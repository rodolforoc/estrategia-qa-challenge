import json
from apichallenge.src.utilities.genericUtilities import generate_random_email_and_password, generate_random_string
from apichallenge.src.utilities.requestsUtility import RequestsUtility


class UserHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_user(self, name=None, email=None, password=None):

        if not name:
            name = 'Test User'
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1!'

        payload = dict()
        payload['name'] = name
        payload['email'] = email
        payload['password'] = password

        create_user_json = self.request_utility.post('auth/register', payload=json.dumps(payload),
                                                     expected_status_code=201)

        return create_user_json

    def login_user(self, email=None, password=None):
        payload = dict()
        payload['email'] = email
        payload['password'] = password

        login_json = self.request_utility.post('auth/authenticate', payload=json.dumps(payload))

        return login_json

    def create_user_wrong_email_password(self, name=None):
        payload = {"name": name}

        req_helper = RequestsUtility()
        rs_api = req_helper.post('auth/register', payload=json.dumps(payload),
                                 expected_status_code=400)

        return rs_api

    def login_user_wrong_credentials(self):

        # random user
        rand_info = generate_random_email_and_password()
        email = rand_info['email']
        password = rand_info['password']
        payload = dict()
        payload['email'] = email
        payload['password'] = password

        # make the call to login
        req_helper = RequestsUtility()
        rs_api = req_helper.post('auth/authenticate', payload=json.dumps(payload), expected_status_code=401)

        return rs_api
