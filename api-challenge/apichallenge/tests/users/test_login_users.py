import pytest
import logging as logger
from apichallenge.src.utilities.genericUtilities import generate_random_email_and_password, generate_random_string
from apichallenge.src.helpers.user_helper import UserHelper


@pytest.mark.user
def test_login_user_with_email_password():
    logger.info("TEST: Login user with email and password")

    # create user
    rand_info = generate_random_email_and_password()
    name = generate_random_string()
    email = rand_info['email']
    password = rand_info['password']
    user_obj = UserHelper()
    user_obj.create_user(name=name, email=email, password=password)

    # make the call to login
    login_api_info = user_obj.login_user(email=email, password=password)

    # verify the name and email in the response
    assert login_api_info['user']['name'] == name, f"Create user returned wrong name. Name: {name}"
    assert login_api_info['user']['email'] == email, f"Create user returned wrong email. Email: {email}"


def test_login_user_with_wrong_email_password():
    logger.info("TEST: Login user with wrong email and password")

    user_obj = UserHelper()
    rs_api = user_obj.login_user_wrong_credentials()

    assert rs_api == "Unauthorized", f"Login user returned the wrong message"
