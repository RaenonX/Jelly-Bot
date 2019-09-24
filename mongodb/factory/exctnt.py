from datetime import datetime
from typing import Union, Optional

from bson import ObjectId

from JellyBot.sysconfig import Database
from flags import ExtraContentType
from models import ExtraContentModel, OID_KEY
from mongodb.factory.results import RecordExtraContentResult, WriteOutcome
from extutils.checker import DecoParamCaster

from ._base import BaseCollection

DB_NAME = "ex"


class ExtraContentManager(BaseCollection):
    database_name = DB_NAME
    collection_name = "content"
    model_class = ExtraContentModel

    def __init__(self):
        super().__init__()
        self.create_index(ExtraContentModel.Timestamp.key,
                          expireAfterSeconds=Database.ExtraContentExpirySeconds, name="Timestamp")

    def record_content(self, type_: ExtraContentType, content: str, title: str = None) -> RecordExtraContentResult:
        if not title:
            title = "-"

        if not content:
            return RecordExtraContentResult(WriteOutcome.X_NOT_EXECUTED)

        model, outcome, ex, insert_result = self.insert_one_data(
            ExtraContentModel, Type=type_, Title=title, Content=content, Timestamp=datetime.utcnow())

        return RecordExtraContentResult(outcome, model, ex)

    @DecoParamCaster({1: ObjectId})
    def get_content(self, content_id: Union[str, ObjectId]) -> Optional[ExtraContentModel]:
        return self.find_one_casted({OID_KEY: content_id}, parse_cls=ExtraContentModel)


_inst = ExtraContentManager()