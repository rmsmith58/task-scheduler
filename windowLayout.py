import PySimpleGUI as sg

mainLayout = [      
          [sg.Text('Create a new task', size=(56, 1)),
           sg.Text('Search tasks')],      
          [sg.Text('Enter task name:', size=(15, 1)),
           sg.InputText(key='name'),
           sg.Radio('Search by name', 'RADIO1', key='nameSearch', default=True),
           sg.Radio('Search by due date', 'RADIO1', key='dateSearch'),
           sg.Radio('Search by category', 'RADIO1', key='categorySearch')],      
          [sg.Text('Enter task due date:', size=(15, 1)),
           sg.InputText(key='date'),
           sg.Text('Enter parameter:', size=(15, 1)),
           sg.InputText(key='parameter')],      
          [sg.Text('Enter task category:', size=(15, 1)),
           sg.InputText(key='category')],
          [sg.Button('Add Task'),
           sg.Text('', size=(56, 1)),
           sg.Button('Search')]      
         ]
'''searchLayout = [
          [sg.Text('Search tasks')],
          [sg.Radio('Search by name', 'RADIO1', default=True),
           sg.Radio('Search by due date', 'RADIO1'),
           sg.Radio('Search by reminder date', 'RADIO1')],
          [sg.Text('Enter parameter', size=(15, 1)), sg.InputText(key='parameter')],
          [sg.Button('Search')]
                ]'''
returnLayout = [
          [sg.Text('Matching tasks:')],
          [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]
               ]

taskSchedulerWindow = sg.Window('Task Scheduler by Ryne Smith').Layout(mainLayout)
#taskSearchWindow = sg.Window('Search tasks - Task scheduler by Ryne Smith').Layout(searchLayout)
taskReturnWindow = sg.Window('Returned tasks - Task scheduler by Ryne Smith').Layout(returnLayout)

'''button1, values1 = taskCreateWindow.Read()
button2, values2 = taskSearchWindow.Read()
button3, values3 = taskReturnWindow.Read()

print(button1, values1)
print(button2, values2)
print(button3, values3)'''
