"""
Этот пример аналогичен url_log_addon_full.py, но записан в короткой форме
"""

import logging
from mitmproxy.http import HTTPFlow


def request(flow: HTTPFlow):
    logging.info(f"call request method for url: {flow.request.pretty_url}")


def response(flow:HTTPFlow):
    logging.info(f"call response method for url: {flow.request.pretty_url}")
