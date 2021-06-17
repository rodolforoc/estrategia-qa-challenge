import pytest
import logging as logger
from apichallenge.src.helpers.project_helper import ProjectHelper
from apichallenge.src.helpers.user_helper import UserHelper


@pytest.mark.projects
def test_get_all_projects():
    logger.info("TEST: Get all projects")

    # get token
    user_obj = UserHelper()
    user_api_info = user_obj.create_user()
    token = user_api_info['token']

    # make the call
    project_helper = ProjectHelper()
    project_api_info = project_helper.get_all_projects(token=token)

    assert project_api_info, f"Get all project endpoint returned nothing."


@pytest.mark.projects
def test_get_project_by_id():
    logger.info("TEST: Get project by id")

    # get token
    user_obj = UserHelper()
    user_api_info = user_obj.create_user()
    token = user_api_info['token']
    user_id = user_api_info['user']['_id']

    # get a product id
    project_helper = ProjectHelper()
    project_api_info = project_helper.create_project(user_id=user_id, token=token)
    project_id = project_api_info['project']['_id']

    # make the call
    project_id_info = project_helper.get_projects_by_id(project_id=project_id, token=token)

    # verify the response
    assert project_id_info['projects']['_id'] == project_id,\
        f"Get project by id returned wrong project. Id:{project_id}"


@pytest.mark.projects
def test_get_project_with_wrong_id():
    logger.info("TEST: Get project with wrong id")

    # get token
    user_obj = UserHelper()
    user_api_info = user_obj.create_user()
    token = user_api_info['token']

    project_helper = ProjectHelper()
    rs_api = project_helper.get_project_wrong_id(token=token)

    # verify the response
    assert rs_api == "Not Found", f"Get project by Id returned the wrong message"

