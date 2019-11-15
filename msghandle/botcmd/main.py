from typing import List

from JellyBot.systemconfig import Bot
from msghandle.models import TextMessageEventObject
from msghandle.botcmd.command import cmd_handler


def handle_bot_cmd_main(e: TextMessageEventObject) -> List[str]:
    # Terminate if empty string / not starts with command prefix
    if not e.content \
            or not e.content.startswith(Bot.Prefix) \
            or (Bot.CaseInsensitivePrefix and e.content.lower().startswith(Bot.Prefix.lower())):
        return []

    return cmd_handler.handle(e)
