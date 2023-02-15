"""
Пример добавления и использования своих собственных опций
"""

from mitmproxy import ctx
from mitmproxy.http import HTTPFlow
from mitmproxy.addonmanager import Loader


def load(loader: Loader):
    loader.add_option(
        name="set_cookie_value",
        typespec=str,
        default="",
        help="Set 'my-test-cookie' cookie with specified value",
    )


def request(flow: HTTPFlow):
    cookies = flow.request.cookies
    cookies["my-test-cookie"] = ctx.options.set_cookie_value
