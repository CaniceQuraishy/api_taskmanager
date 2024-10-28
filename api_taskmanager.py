class Task:
    def __init__(self, title, description, due_date):
        self.title = title          # Title of the task
        self.description = description  # Description of the task
        self.due_date = due_date    # Due date for the task
        self.is_completed = False    # Status of the task, set to not completed initially

    def mark_as_completed(self):
        self.is_completed = True  # Set the task status as completed