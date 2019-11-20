from django.utils.translation import gettext_lazy as _

from flags import BotFeature
from msghandle.models import TextMessageEventObject, HandledMessageEventText

from ._base_ import CommandNode

cmd = CommandNode(
    codes=["help"], order_idx=1000, name=_("Help"),
    description=_("See the documentation or bot related information."))


@cmd.command_function(feature_flag=BotFeature.TXT_BOT_HELP)
def help_text(e: TextMessageEventObject):
    return [
        HandledMessageEventText(
            content=_("LINE BOT:\n"
                      "Beta: http://rnnx.cc/LineBeta\n"
                      "Stable: http://rnnx.cc/LineStable\n"
                      "\n"
                      "Discord:\n"
                      "Beta: http://rnnx.cc/DiscordBeta\n"
                      "Stable: http://rnnx.cc/DiscordStable\n"
                      "\n"
                      "Website:\n"
                      "Beta: http://rnnx.cc/WebsiteBeta\n"
                      "Stable: http://rnnx.cc/WebsiteStable"),
            bypass_multiline_check=True
        )
    ]