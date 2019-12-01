import PySimpleGUI as sg

mainLayout = [      
          [sg.Text('Create a new task', size=(56, 1))],      
          [sg.Text('Enter task name:', size=(15, 1)),
           sg.InputText(key='name')],      
          [sg.Text('Enter task due date:', size=(15, 1)),
           sg.InputText(key='date')],      
          [sg.Text('Enter task category:', size=(15, 1)),
           sg.InputText(key='category')],
          [sg.Button('Add Task'),
           sg.Text('', key='addOutput', size=(56, 1))],
          [sg.Text('Search tasks')],
          [sg.Radio('Search by name', 'RADIO1', key='nameSearch', default=True),
           sg.Radio('Search by due date', 'RADIO1', key='dateSearch'),
           sg.Radio('Search by category', 'RADIO1', key='categorySearch')],
          [sg.Text('Enter parameter:', size=(15, 1)),
           sg.InputText(key='parameter')],
          [sg.Button('Search'),
           sg.Text('', key='searchOutput')],
          [sg.Text('Search Results')],
          [sg.Listbox(values=[], size=(30, 6), key='searchReturn')]
         ]

taskSchedulerWindow = sg.Window('Task Scheduler by Ryne Smith').Layout(mainLayout)
