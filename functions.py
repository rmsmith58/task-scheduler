import pickle as p
import os
import taskClass as t

#write task class to file
def writeTask(title, date, remind):
    tempTask = t.task(title, date, remind)
    p.dump(tempTask, open(('tasks\%s.p' % tempTask.getName()), 'wb'))
    
#printd all tasks wirh matching due date
def readTaskDate(date):
    output = ''
    files = os.listdir('tasks')
    for filename in files:
        temp = p.load(open('tasks\%s' % filename, 'rb'))
        if temp.getDate() == date:
            output += temp.display()
            output += '\n'
    if output == '':
        output += 'No matching tasks found'
    else:
        output = 'Found tasks:\n' + output    
    print(output + '--------')

#prints all tasks with matching reminder date
def readTaskRemind(reminder):
    output = ''
    files = os.listdir('tasks')
    for filename in files:
        temp = p.load(open('tasks\%s' % filename, 'rb'))
        if temp.getRemind() == reminder:
            output += temp.display()
            output += '\n'
    if output == '':
        output += 'No matching tasks found'
    else:
        output = 'Found tasks:\n' + output
    print(output + '--------')

#prints all tasks with matching name
def readTaskName(name):
    output = ''
    files = os.listdir('tasks')
    for filename in files:
        temp = p.load(open('tasks\%s' % filename, 'rb'))
        if temp.getName() == name:
            output += temp.display()
            output += '\n'
    if output == '':
        output += 'No matching tasks found'
    else:
        output = 'Found tasks:\n' + output
    print(output + '--------')

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
    
#run readTask with given search parameter and term
def searchTask():
    print('Enter search parameter: Name, date, or reminder')
    key = input('PARAMETER>')
    if key.lower() == 'name':
        readTaskName(input('Enter search term\nNAME>'))
    elif key.lower() == 'date':
        readTaskDate(input('Enter search term\nDATE>'))
    elif key.lower() == 'reminder':
        readTaskRemind(input('Enter search term\nREMINDER>'))
    else:
        print('Unrecognized search parameter')
