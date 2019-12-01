import functions as fn
import windowLayout as wl

#main loop
while True:
    event, values = wl.taskSchedulerWindow.Read()
    wl.taskSchedulerWindow['addOutput'].update('')
    if event is None:
        break
    if event == 'Add Task':
        #writes task with given input and clears the input boxes
        fn.writeTask(values['name'], values['date'], values['category'])
        wl.taskSchedulerWindow['addOutput'].update('~Task added successfully!~')
        wl.taskSchedulerWindow['name'].update('')
        wl.taskSchedulerWindow['date'].update('')
        wl.taskSchedulerWindow['category'].update('')
    if event == 'Search':
        #each of the below statements updates the search return list box with the search function output
        if values['nameSearch']:
            wl.taskSchedulerWindow['searchReturn'].update(fn.readTaskName(values['parameter']))
        elif values['dateSearch']:
            wl.taskSchedulerWindow['searchReturn'].update(fn.readTaskDate(values['parameter']))
        else:
            wl.taskSchedulerWindow['searchReturn'].update(fn.readTaskCategory(values['parameter']))
            
wl.taskSchedulerWindow.close()
