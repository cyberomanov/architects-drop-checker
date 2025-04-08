import json
import random
import time

import requests
from loguru import logger


def get_proxied_session(proxy: str = None, headers_update: bool = False):
    session = requests.Session()
    if proxy:
        session.proxies = {
            'http': proxy,
            'https': proxy
        }
    if headers_update:
        session.headers.update({'Content-Type': 'application/octet-stream'})
    session.request = lambda *args, **kwargs: requests.Session.request(session, *args, **kwargs)
    return session


def process_request(
    session: requests.Session, 
    url: str, 
    payload: dict = None,
    max_retries: int = 20, 
    do_not_log: bool = False,
    post: bool = False
):
    response = None
    for attempt in range(max_retries):
        try:
            response = session.post(url=url, json=payload) if post else session.get(url=url, json=payload) 
            if response.status_code == 200 or response.status_code == 404:
                return json.loads(response.content)
            else:
                time.sleep(random.randint(1, 5))
        except requests.RequestException as e:
            time.sleep(random.randint(1, 5))

    if not do_not_log:
        logger.error(f"all {max_retries} attempts failed for: {url}, {payload}, {response if response else ''}")
    return None
