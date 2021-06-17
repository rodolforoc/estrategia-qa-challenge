import pytest
import logging as logger
from apichallenge.src.helpers.project_helper import ProjectHelper
from apichallenge.src.helpers.user_helper import UserHelper

@pytest.mark.projects
def test_delete_project_by_id():
    logger.info("TEST: Delete a project by ID")

    # get token
    user_obj = UserHelper()
    user_api_info = user_obj.create_user()
    token = user_api_info['token']
    user_id = user_api_info['user']['_id']

    # create a project
    project_helper = ProjectHelper()
    project_api_info = project_helper.create_project(user_id=user_id, token=token)
    project_id = project_api_info['project']['_id']

    # make the delete call
    rs_api = project_helper.delete_projects_by_id(project_id=project_id, token=token)

    assert rs_api == {}, "The delete response should be empty"
