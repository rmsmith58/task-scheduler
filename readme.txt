Ryne Smith
CSCI 101 Section G
Create Project

Task scheduler program with GUI

-IMPORTANT- This program requires PySimpleGUI to run. Instructions for install here https://pypi.org/project/PySimpleGUI/

Program is run from taskScheduler.py

This is a simple program to create and access task items from a GUI. On run, two windows are created to allow creation of new tasks and searching of saved
tasks.

Creating Tasks
	The creation window allows the user to input three values to create a new task: name, due date, and category. These values are used to create
	a new instance of a task object. This object is then saved as a file using pickle to allow for data storage. The location for saved tasks is
	the "tasks" folder in the root directory of the program.

Searching Tasks
	The search window allows the user to search through previously created tasks. The user selects the task value to search by (name, due date, or category)
	and inputs a parameter for the search. The program then opens and searches all tasks in the tasks folder and returns any matching tasks in a new window.

Task Management
	To limit the number of saved tasks, the program runs a function on startup to delete any tasks that have a due date earlier than the current
	system time date. Functionality to allow the user to manually delete tasks was considered but could not be included due to time constraints.