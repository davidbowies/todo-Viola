# To-Do List App

The To-Do List App is a private to-do list that helps users organize and manage their tasks. The app is built using Python, Flask and SQLite.

## Key Features

The To-Do List App includes the following features:

- Overview Tasks: Provides an overview of all the tasks on the landing page.
- On the landing page: subpages called studies, private and general.
- The studies page has more subpages which are currently not working.
- Private page: you can create, update, delete a task. While you hover over a task you even have a short overview of the task created. You can also click on the created task.
- General page: you can create, update, delete a task. While you hover over a task you even have a short overview of the task created. You can also click on the created task.

## Data Models

### Task Model

The Task model represents a task that needs to be completed. It has the following properties:

- `id`: The unique ID of the task (integer).
- `title`: The title of the task (string).
- `description`: A description of the task (text).
- `whendue`: The due date of the task (datetime).
- `completed`: A boolean value indicating whether the task has been completed (boolean).
- `categories`: A list of categories associated with the task (relationship).

### Category Model

The Category model represents a category that can be associated with tasks. It has the following properties:

- `id`: The unique ID of the category (integer).
- `name`: The name of the category (string).

### Task Categories Model

The TaskCategories model represents the many-to-many relationship between tasks and categories. It has the following properties:

- `task_id`: The ID of the task (integer).
- `category_id`: The ID of the category (integer).

### Tag Model

The Tag model represents a tag that can be associated with tasks. It has the following properties:

- `id`: The unique ID of the tag (integer).
- `name`: The name of the tag (string).

### Task Tags Model

The TaskTags model represents the many-to-many relationship between tasks and tags. It has the following properties:

- `task_id`: The ID of the task (integer).
- `tag_id`: The ID of the tag (integer).

## Tech Stack

The To-Do List App is built using Python, Flask, and SQLite and a little bit of JavaScript as well.

## Installation

To run the app, follow these steps:

1. Clone this repository to your local machine: `git clone https://github.com/davidbowies/todo-Viola.git`.
2. Create a virtual environment: `python3 -m venv venv`.
3. Activate the virtual environment: `source venv/bin/activate`.
4. Install the required packages: `pip install flask`.
5. Run the app: `gunicorn run:app`.
6. When you're done using the app, deactivate the virtual environment: `deactivate`.
