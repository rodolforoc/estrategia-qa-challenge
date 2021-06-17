import pytest
import logging as logger
from apichallenge.src.helpers.project_helper import ProjectHelper
from apichallenge.src.helpers.user_helper import UserHelper
from apichallenge.src.utilities.genericUtilities import generate_random_string


@pytest.mark.projects
def test_create_project():
    logger.info("TEST: Create Project")

    # get token
    user_obj = UserHelper()
    user_api_info = user_obj.create_user()
    token = user_api_info['token']
    user_id = user_api_info['user']['_id']

    # create the payload variables
    title = 'Title ' + generate_random_string()
    description = 'Description ' + generate_random_string()
    task_name = 'Task ' + generate_random_string()

    # make the call
    project_helper = ProjectHelper()
    project_api_info = project_helper.create_project(title=title, description=description, task_name=task_name,
                                                     user_id=user_id, token=token)

    # verify the response
    assert project_api_info['project']['tasks'][0]['name'] == task_name, \
        f"Create project returned wrong name. Name: {task_name}"
    assert project_api_info['project']['tasks'][0]['assignedTo'] == user_id, \
        f"Create project returned wrong userId. userId: {user_id}"
    assert project_api_info['project']['title'] == title, f"Create project returned wrong title. Title: {title}"
    assert project_api_info['project']['description'] == description, \
        f"Create project returned wrong description. Description: {description}"
