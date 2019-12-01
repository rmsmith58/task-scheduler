import functions as fn
import windowLayout as wl

commandList = {
    'help' : fn.printHelp,
    'add' : fn.addTask,
    'search' : fn.searchTask
    }

#main
while True:
    event, values = wl.taskSchedulerWindow.Read()
    if event is None:
        break
    if event == 'Add Task':
        fn.writeTask(values['name'], values['date'], values['category'])
        #TODO reset input boxes
    if event == 'Search':
        if values['nameSearch']:
            readTaskName(values['parameter'])
        elif values['dateSearch']:
            readTaskDate(values['parameter'])
        else:
            readTaskCategory(values['parameter'])
    print('loop')
wl.taskSchedulerWindow.close()
