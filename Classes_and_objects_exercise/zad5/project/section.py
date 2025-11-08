from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        task = next((t for t in self.tasks if t.name == task_name), None)
        if task not in self.tasks:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        tasks_amount = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {tasks_amount - len(self.tasks)} tasks."

    def view_section(self) -> str:
        return (f"Section {self.name}:" +
                "".join(f"\n{task.details()}" for task in self.tasks))