"""
Простой аддон, заменяющий содержимое ответа с "Example Domain", на "Custom Domain"
"""

from mitmproxy.http import HTTPFlow


def response(flow: HTTPFlow):
    response = flow.response
    response.content = response.content.replace(
        b"Example Domain",
        b"Custom Domain"
    )
