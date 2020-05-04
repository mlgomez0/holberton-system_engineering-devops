#0x15. API

## Concepts

- Requests with python
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- How to use APIs

## Usage

Educational purposes

## Tasks

0. 0-gather_data_from_an_API.py: Python script that, using this REST API(https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress:
- The script must accept an integer as a parameter, which is the employee ID
- First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
1. 1-export_to_CSV.py: Extends the Python script to export data in the CSV format. Requirements:
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
2. 2-export_to_JSON.py: Extends the Python script to export data in the JSON format. Requirements:
- Records all tasks that are owned by this employee
- Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}
- File name must be: USER_ID.json
3. 3-dictionary_of_list_of_dictionaries.py: Extends the Python script to export data in the JSON format. Requirements:
- Records all tasks from all employees Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
- File name must be: todo_all_employees.json
