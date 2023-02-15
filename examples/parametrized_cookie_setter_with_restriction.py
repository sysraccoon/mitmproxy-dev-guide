"""
Усложнённый вариант parametrized_cookie_setter.py в котором добавлена валидация выставленной опции
"""

from typing import Optional
from mitmproxy import ctx
from mitmproxy.http import HTTPFlow
from mitmproxy.addonmanager import Loader
from mitmproxy.exceptions import OptionsError


COOKIE_VALUE_MIN_LENGTH = 5


def load(loader: Loader):
    loader.add_option(
        name="set_cookie_value",
        typespec=Optional[str],
        default=None,
        help=f"Set 'my-test-cookie' cookie with specified value. Expected length {COOKIE_VALUE_MIN_LENGTH} or greater",
    )


def configure(updates: dict):
    if "set_cookie_value" not in updates:
        return

    new_value = ctx.options.set_cookie_value
    
    if new_value is not None and len(new_value) < COOKIE_VALUE_MIN_LENGTH:
        raise OptionsError(f"set_cookie_value must have length {COOKIE_VALUE_MIN_LENGTH} or more")



def request(flow: HTTPFlow):
    cookie_value = ctx.options.set_cookie_value

    if not cookie_value:
        return

    cookies = flow.request.cookies
    cookies["my-test-cookie"] = cookie_value
