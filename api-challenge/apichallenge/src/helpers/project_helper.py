import json
from apichallenge.src.utilities.requestsUtility import RequestsUtility
from apichallenge.src.utilities.genericUtilities import generate_random_string


class ProjectHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_project(self, title=None, description=None, task_name=None, user_id=None, token=None):

        # create the payload variables
        if not title:
            title = 'Title ' + generate_random_string()
        if not description:
            description = 'Description ' + generate_random_string()
        if not task_name:
            task_name = 'Task ' + generate_random_string()

        tasks = [
            {
                "name": task_name,
                "assignedTo": user_id
            }
        ]

        headers = dict()
        headers['content-type'] = "application/json"
        headers['authorization'] = "Bearer " + token

        payload = dict()
        payload['title'] = title
        payload['description'] = description
        payload['tasks'] = tasks

        create_project_json = self.request_utility.post('projects', payload=json.dumps(payload), headers=headers,
                                                        expected_status_code=201)

        return create_project_json

    def get_all_projects(self, token=None):
        headers = dict()
        headers['content-type'] = "application/json"
        headers['authorization'] = "Bearer " + token

        all_projects_json = self.request_utility.get('projects', headers=headers)

        return all_projects_json

    def get_projects_by_id(self, project_id=None, token=None):
        headers = dict()
        headers['content-type'] = "application/json"
        headers['authorization'] = "Bearer " + token

        project_json = self.request_utility.get(f'projects/{project_id}', headers=headers)

        return project_json

    def delete_projects_by_id(self, project_id=None, token=None):
        headers = dict()
        headers['content-type'] = "application/json"
        headers['authorization'] = "Bearer " + token

        project_json = self.request_utility.delete(f'projects/{project_id}', headers=headers)

        return project_json

    def update_projects_by_id(self, project_id=None, task_updated=None, token=None):
        headers = dict()
        headers['content-type'] = "application/json"
        headers['authorization'] = "Bearer " + token

        project_updated_json = self.request_utility.put(f'projects/{project_id}', payload=json.dumps(task_updated),
                                                        headers=headers)

        return project_updated_json

    def get_project_wrong_id(self, token=None):
        headers = dict()
        headers['content-type'] = "application/json"
        headers['authorization'] = "Bearer " + token

        # random project id
        wrong_project_id = generate_random_string()

        req_helper = RequestsUtility()
        rs_api = req_helper.get(f'projects/{wrong_project_id}', headers=headers, expected_status_code=404)

        return rs_api

    def update_project_wrong_id(self, user_id=None, token=None):
        headers = dict()
        headers['content-type'] = "application/json"
        headers['authorization'] = "Bearer " + token

        # random project id
        wrong_project_id = generate_random_string()

        task_new_name = 'Updated Task ' + generate_random_string()

        task_updated = [
            {
                "name": task_new_name,
                "assignedTo": user_id
            }
        ]

        req_helper = RequestsUtility()
        rs_api = req_helper.put(f'projects/{wrong_project_id}', payload=json.dumps(task_updated),
                                headers=headers, expected_status_code=404)

        return rs_api
