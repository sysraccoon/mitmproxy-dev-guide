"""
Усложнённый вариант parametrized_cookie_setter.py в котором добавлена валидация выставленной опции
"""

from mitmproxy.http import HTTPFlow
from mitmproxy.addonmanager import Loader
from mitmproxy import ctx
from mitmproxy.exceptions import OptionsError
from typing import Optional


COOKIE_MIN_LENGTH = 5


def load(loader: Loader):
    loader.add_option(
        name="set_cookie_value",
        typespec=Optional[str],
        default=None,
        help="Set 'my-test-cookie' cookie with specified value\n" +
             "Expect length {COOKIE_MIN_LENGTH} or greater",
    )


def configure(updates: set):
    if "set_cookie_value" not in updates:
        return

    new_value = ctx.options.set_cookie_value

    if new_value is None:
        return
    if len(new_value) >= COOKIE_MIN_LENGTH:
        return
    
    raise OptionsError(f"len(set_cookie_value) < {COOKIE_MIN_LENGTH}")


def request(flow: HTTPFlow):
    cookie_value = ctx.options.set_cookie_value

    if not cookie_value:
        return

    cookies = flow.request.cookies
    cookies["my-test-cookie"] = cookie_value
