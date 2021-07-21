tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# 1. Print a list of uncompleted tasks
# def list_of_uncompleted_tasks(tasks):
#     uncompleted_tasks = []
#     for task in tasks:
#         if task["completed"] == False:
#             uncompleted_tasks.append(task)
#     return uncompleted_tasks

# print(list_of_uncompleted_tasks(tasks))

# 2. Print a list of completed tasks
# def list_of_completed_tasks(tasks):
#     completed_tasks = []
#     for task in tasks:
#         if task["completed"] == True:
#             completed_tasks.append(task)
#     return completed_tasks

# print(list_of_completed_tasks(tasks))

# 3. Print a list of all task descriptions

# def all_descriptions(tasks):
#     descriptions = []
#     for item in tasks:
#         descriptions.append(item["description"])
#     return descriptions

# print(all_descriptions(tasks))
        
# 4. Print a list of tasks where time_taken is at least a given time
# def time_taken(tasks, number):
#     long_tasks = []
#     for item in tasks:
#         if int(item["time_taken"]) >= number:
#             long_tasks.append(item["description"])
#     return long_tasks

# print(time_taken(tasks, 20))

# 5. Print any task with a given description
def task_from_description(input):
    input_lower_case = input.lower()
    for task in tasks:
        if input_lower_case == task["description"].lower():
            return task
        else:
            return "No task found"

print(task_from_description("wAsh DIshes"))

