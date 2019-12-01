Ryne Smith
CSCI 101 Section G
Create Project

Task scheduler program with GUI

-IMPORTANT- This program requires PySimpleGUI to run. Instructions for install here https://pypi.org/project/PySimpleGUI/

Pickle is also required but is included with the most recent version of Python 3.

To access the program, run taskScheduler.py

This is a simple program to create and access task items from a GUI. The window has three sections: the task creation section,
the task search section, and the search output section.

The task creation section allows the user to create new tasks with 3 parameters: name, date, and category. These can be left blank
but this will make finding them harder. The input values are then passed into a new task object, which is then saved as its own file
with pickle.

The task search section allows the user to find previously created tasks by choosing one of three parameters and inputting a value.
The program will then search each saved task object and return a list of matching items.

Any returned values from the search will be listed in the search output section.




