from apichallenge.src.configs.hosts_config import API_HOSTS
import requests
import os
import logging as logger

class RequestsUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    # verify status code of the call
    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code." \
            f"Expected {self.expected_status_code}, Actual status code: {self.status_code}" \
            f"URL: {self.url}, Response Json: {self.rs_json}"


    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API POST response: {self.rs_json}")

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API GET response: {self.rs_json}")

        return self.rs_json

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API PUT response: {self.rs_json}")

        return self.rs_json

    def delete(self, endpoint, headers=None, expected_status_code=204):

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API DELETE response: {self.rs_json}")

        return self.rs_json