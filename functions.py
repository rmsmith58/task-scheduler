import pickle as p
import os
import taskClass as t

#write task class to file
def writeTask(title, date, remind):
    tempTask = t.task(title, date, remind)
    p.dump(tempTask, open(('tasks\%s.p' % tempTask.getName()), 'wb'))
    
#returns list of all task objects in folder
def readTask(date):
    output = []
    files = os.listdir('tasks')
    for filename in files:
        temp = p.load(open('tasks\%s' % filename, 'rb'))
        output.append(temp)
    return output
        

#print list of commands
def printHelp():
    print('help - list commands')
    print('add - add task')
    print('search - list tasks')
    print('stop - stop program\n--------')

#get input and call writeTask with that input
def addTask():
    print('Enter name of task')
    name = input('NAME>')
    print('Enter task date (MM/DD/YYYY)')
    taskDate = input('DATE>')
    print('Enter date for reminder (MM/DD/YYYY)')
    remindDate = input('DATE>')

    writeTask(name, taskDate, remindDate)

    print('Task added successfully\n--------')
    
#run readTask with date input
def searchTask():
    print('Enter date to search (MM/DD/YYYY)')
    date = input('DATE>')

    print('%s\n--------' % readTask(date))
    
