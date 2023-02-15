"""
Пример добавления своей собственной команды.
Подробнее про команды можно почитать тут:
https://docs.mitmproxy.org/stable/concepts-commands/
"""

from collections.abc import Sequence
from mitmproxy.command import command
from mitmproxy.http import HTTPFlow
from mitmproxy.flow import Flow

@command("custom_command.add_cookie")
def add_cookie(
    flows: Sequence[Flow],
    name: str,
    value: str,
):
    for flow in flows:
        if not isinstance(flow, HTTPFlow):
            continue
        cookies = flow.request.cookies
        cookies.add(name, value)


# Не документированный вариант добавления хоткея для своих команд
# Если хотите использовать более надёжный вариант, можете посмотреть содержимое keys.yaml

# from mitmproxy import ctx


# def load(loader):
#     ctx.master.keymap.add(
#         "c",
#         "console.command custom_command.add_cookie @focus ",
#         ["flowlist", "flowview"],
#         "Add cookie with specified name+value",
#     )
