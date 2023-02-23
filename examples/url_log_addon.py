"""
Этот пример аналогичен url_log_addon_full.py, но записан в короткой форме
"""

import logging
from mitmproxy.http import HTTPFlow


def request(flow: HTTPFlow):
    logging.info("call request method")


def response(flow:HTTPFlow):
    logging.info("call response method")
