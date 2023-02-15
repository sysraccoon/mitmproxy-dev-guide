"""
Простой пример выставляющий куку во все запросы
"""

from mitmproxy.http import HTTPFlow


def request(flow: HTTPFlow):
    cookies = flow.request.cookies
    cookies["my-test-cookie"] = "some-cookie-value"
