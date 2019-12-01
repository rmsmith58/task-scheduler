import pickle as p
import os
import taskClass as t
import random

#write task class to file
def writeTask(title, date, remind):
    random.seed()
    tempTask = t.task(title, date, remind)
    p.dump(tempTask, open(('tasks\%s.p' % random.randrange(999999999999)), 'wb'))
    
#printd all tasks wirh matching due date
def readTaskDate(date):
    output = ['Name:   Date:   Category:']
    files = os.listdir('tasks')
    for filename in files:
        temp = p.load(open('tasks\%s' % filename, 'rb'))
        if temp.getDate() == date:
            output.append(temp.display())
    if len(output) == 1:
        output.append('No matching tasks found')
    return output    

#prints all tasks with matching reminder date
def readTaskCategory(category):
    output = ['Name:   Date:   Category:']
    files = os.listdir('tasks')
    for filename in files:
        temp = p.load(open('tasks\%s' % filename, 'rb'))
        if temp.getCategory() == category:
            output.append(temp.display())
    if len(output) == 1:
        output.append('No matching tasks found')
    return output

#prints all tasks with matching name
def readTaskName(name):
    output = ['Name:   Date:   Category:']
    files = os.listdir('tasks')
    for filename in files:
        temp = p.load(open('tasks\%s' % filename, 'rb'))
        if temp.getName() == name:
            output.append(temp.display())
    if len(output) == 1:
        output[0] = 'No matching tasks found'
    return output
