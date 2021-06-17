import pytest
import logging as logger
from apichallenge.src.helpers.project_helper import ProjectHelper
from apichallenge.src.helpers.user_helper import UserHelper
from apichallenge.src.utilities.genericUtilities import generate_random_string


@pytest.mark.projects
def test_update_project_by_id():
    logger.info("TEST: Update project by ID")

    # get token
    user_obj = UserHelper()
    user_api_info = user_obj.create_user()
    token = user_api_info['token']
    user_id = user_api_info['user']['_id']

    # create project
    title = 'Title ' + generate_random_string()
    description = 'Description ' + generate_random_string()

    # make the call
    project_helper = ProjectHelper()
    project_api_info = project_helper.create_project(title=title, description=description,
                                                     user_id=user_id, token=token)
    project_id = project_api_info['project']['_id']

    task_new_name = 'Updated Task ' + generate_random_string()

    task_updated = [
        {
            "name": task_new_name,
            "assignedTo": user_id
        }
    ]

    update_json = project_helper.update_projects_by_id(project_id=project_id, taskUpdated=task_updated, token=token)

    assert update_json['project']['tasks'][0]['name'] == task_new_name, \
        f"Update project returned wrong name. Name: {task_new_name} "
    assert update_json['project']['title'] == title, f"Update project returned wrong title. Title: {title} ."
    assert update_json['project']['description'] == description, f"Update project returned the wrong description. " \
                                                                 f"Description: {description}."


@pytest.mark.projects
def test_update_project_with_wrong_id():
    logger.info("TEST: Update project with wrong ID")

    # get token
    user_obj = UserHelper()
    user_api_info = user_obj.create_user()
    token = user_api_info['token']
    user_id = user_api_info['user']['_id']

    project_helper = ProjectHelper()
    rs_api = project_helper.update_project_wrong_id(user_id=user_id, token=token)

    # verify the response
    assert rs_api == "Not Found", f"Get project by Id returned the wrong message"
