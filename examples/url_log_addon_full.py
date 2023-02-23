"""
Пример базового аддона для mitmproxy записанного в полной форме.
Короткая форма показана в url_log_addon.py
"""

import logging
from mitmproxy.http import HTTPFlow


class UrlLogAddon:
    def request(self, flow: HTTPFlow):
        logging.info(f"call request method")
    
    def response(self, flow: HTTPFlow):
        logging.info(f"call response method")


addons = [UrlLogAddon()]
