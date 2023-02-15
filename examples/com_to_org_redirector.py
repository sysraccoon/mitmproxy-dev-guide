"""
Пример подменяющий домен .com на .org во всех запросах
"""

import re
import logging
from mitmproxy.http import HTTPFlow

def request(flow: HTTPFlow):
    original_host = flow.request.pretty_host
    new_host = re.sub(r"\.com$", ".org", original_host)

    flow.request.host = new_host

    logging.info(f"replace host {original_host} to {new_host}")
