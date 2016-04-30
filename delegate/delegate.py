import asana
import constants

# Create class Delegator that accepts a list of tasks to delegate
# Task format is {'project': [project_id], 'name': str_task_name, 'assignee': 'email'}

class Delegator(object):

    def __init__(self, tasks=[]):
        self.tasks = tasks
        self.created_tasks = []
        self.asana = self.build_asana_client()

    def build_asana_client(self):
        return asana.Client.access_token(constants.CEO_ACCESS_TOKEN)

    def assign_task_owners(self):
        #TODO: Add a more interesting task assignment mechanism
        # But for now, Max can take it all
        for task in self.tasks:
            if "assignee" not in task:
                task["assignee"] = constants.MAX_EMAIL

    def create_tasks(self):
        for _ in self.tasks:
            created_task = self.asana.tasks.create_in_workspace(
                            constants.WORKSPACE_ID,
                            self.tasks.pop(0))
            self.created_tasks.append(created_task)

    def delegate(self):
        self.assign_task_owners()
        self.create_tasks()
