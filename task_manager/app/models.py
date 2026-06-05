from datetime import datetime

class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.done = False
        self.created_at = datetime.now()

    def mark_done(self):
        self.done = True

    def to_dict(self) -> dict:
        return {'id': self.id,
                'title': self.title,
                'done': self.done,
                'crested_at': self.created_at
                }

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done,
            'created_at': self.created_at.isoformat()
        }
    
class TaskManager:
    def __init__(self):
        self.tasks: dict[int, Task] = {}
        self.next_id = 1

    def list_all(self):
        return [t.to_dict() for t in self.tasks.values()]

    def add(self, title: str) -> Task:
        task = Task(self.next_id, title)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def mark_done(self, task_id: int) -> Task | None:
        task = self.tasks.get(task_id)
        if task is None:
            return None
        task.mark_done()
        return task