# -*- coding: utf-8 -*-

# ------------------------------------
# file: reuse_methods.py
# author: panhui
# time: 2018-06-04 17:01 
# ------------------------------------

import requests
from src.utils.log import logger


def request(method, url, data):
    """
    http request method.
    :param method: GET/POST
    :param url: http url
    :param data: data/params, dict-like
    :return: http response
    """
    session = requests.Session()
    try:
        if method.upper() == 'POST':
            r = session.post(url, data=eval(data))
            session.close()
        elif method.upper() == 'GET':
            r = session.get(url, params=eval(data))
            session.close()
        else:
            raise TypeError("unsupported method", method)
        return r
    except Exception as e:
        logger.error("request error: %s", e)
