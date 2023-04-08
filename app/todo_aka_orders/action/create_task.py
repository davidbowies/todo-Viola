from app.todo_aka_orders.models import Tag, TaskTag, Note

def create_task(form_data, tasks):
    #create a task
    task = Tag()
    task.save

    #create Note
    note = Note(
        body=form_data.get('body'),
        created_at=form_data.get('created_at'),
        task=task
    )
    note.save()

    # create to do list
    for task in tasks:
        number_of_tasks = form_data.get(task.slug, 0)

        if int(number_of_tasks) > 0:
            todo_list = TaskTag(
                tasks = tasks,
                task = task,
                number_of_tasks=number_of_tasks
            )
            todo_list.save()

