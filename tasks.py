class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.status = "Pending"
        self.priority = priority
        self.due_date = due_date

    def complete(self):
        self.status = "Completed"

    def reopen(self):
        self.status = "Pending"

    def edit(self, new_title):
        self.title = new_title

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date
        }