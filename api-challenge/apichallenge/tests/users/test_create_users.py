import pytest
import logging as logger
from apichallenge.src.utilities.genericUtilities import generate_random_email_and_password, generate_random_string
from apichallenge.src.helpers.user_helper import UserHelper


@pytest.mark.user
def test_create_user_with_email_password():
    logger.info("TEST: Create new user with email and password")

    rand_info = generate_random_email_and_password()
    name = generate_random_string()
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    user_obj = UserHelper()
    user_api_info = user_obj.create_user(name=name, email=email, password=password)

    # verify the name and email in the response
    assert user_api_info['user']['name'] == name, f"Create user returned wrong name. Name: {name}"
    assert user_api_info['user']['email'] == email, f"Create user returned wrong email. Email: {email}"


def test_create_user_with_missing_email_password():
    logger.info("TEST: Create new user with missing email and password")
    name = generate_random_string()

    user_obj = UserHelper()

    rs_api = user_obj.create_user_wrong_email_password(name=name)

    assert rs_api == "Bad Request", f"Create user returned the wrong message"
