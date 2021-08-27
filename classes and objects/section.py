from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'
        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str):
        searched_task = [t for t in self.tasks if t.name == task_name]
        if searched_task:
            s = searched_task[0]
            s.completed = True
            return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        not_completed_tasks = [t for t in self.tasks if not t.completed]
        removed_tasks = len(self.tasks) - len(not_completed_tasks)
        self.tasks = not_completed_tasks
        return f'Cleared {removed_tasks} tasks.'

    def view_section(self):
        details = [f'\n{t.details()}' for t in self.tasks]
        return f'Section {self.name}:{"".join(details)}'


task = Task('Make bed', '27/05/2020')
print(task.change_name('Go to Univercity'))
print(task.change_due_date('28.05.2020'))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section('Daily tasks')
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
