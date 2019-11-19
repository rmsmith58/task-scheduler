import functions as fn

#main loop variable
main = True

#stop function for program
def stop():
    global main
    main = False

commandList = {
    'help' : fn.printHelp,
    'add' : fn.addTask,
    'search' : fn.searchTask,
    'stop' : stop
    }

#main
print('Welcome to task scheduler')
while(main):
    print('Enter help for list of commands')
    print('Enter stop to stop program')
    commandList.get(input('COMMAND>'), lambda : print('Command not recognized\n--------'))()
print('Task scheduler closing')
