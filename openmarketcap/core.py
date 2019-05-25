#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import tempfile
import logging
import requests_cache


class Market(object):
    _session = None
    __DEFAULT_BASE_URL = 'http://api.openmarketcap.com/api/v1/'
    __DEFAULT_TIMEOUT = 30
    __TEMPDIR_CACHE = True

    __DEFAULT_CACHE_EXPIRY_TIME = 60  # in seconds

    def __init__(self, base_url=__DEFAULT_BASE_URL, request_timeout=__DEFAULT_TIMEOUT,
                 tempdir_cache=__TEMPDIR_CACHE):
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.cache_filename = 'openmarketcap_cache'
        self.cache_name = os.path.join(tempfile.gettempdir(),
                                       self.cache_filename) if tempdir_cache else self.cache_filename

    @property
    def session(self):
        if not self._session:
            self._session = requests_cache.core.CachedSession(cache_name=self.cache_name,
                                                              backend='sqlite',
                                                              expire_after=self.__DEFAULT_CACHE_EXPIRY_TIME)
            self._session.headers.update({'Content-Type': 'application/json'})
            self._session.headers.update({'User-agent': 'openmarketcap - python wrapper around openmarketcap.com (github.com/12Siva/openmarketcap-py)'})

        return self._session

    def __request(self, endpoint, params):
        response_object = self.session.get(self.base_url + endpoint, params=params, timeout=self.request_timeout)

        try:
            response = json.loads(response_object.text)

            if isinstance(response, list) and response_object.status_code == 200:
                response = [dict(item, **{u'cached': response_object.from_cache}) for item in response]
            if isinstance(response, dict) and response_object.status_code == 200:
                response[u'cached'] = response_object.from_cache

        except Exception as exception:
            logging.error(f'Encountered error for endpoint {endpoint}.')
            return exception

        return response
