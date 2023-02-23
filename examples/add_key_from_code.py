"""
Не документированный вариант добавления хоткея для своих команд
Если хотите использовать более надёжный вариант, можете посмотреть содержимое keys.yaml
"""

from mitmproxy import ctx


def load(loader):
    ctx.master.keymap.add(
        "c",
        "console.command custom_command.add_cookie @focus ",
        ["flowlist", "flowview"],
        "Add cookie with specified name+value",
    )
