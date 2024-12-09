# Alec Porter Lab 10

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pickle
import datetime


# convert time integers from sliders to single time string in format HH:MM
def convTime(hour, minute):     

    if hour==0:
        hour='0'+str(hour)
    else:
        hour = str(hour)
    if minute==0 or minute==5:
        minute='0'+str(minute)
    else:
        minute=str(minute)
    time = hour + ':' + minute
    return time


# check data fields for blanks or date error
def checkFields(x, y, z):

    # check for blanks
    if x == '':
        messagebox.showerror('Error','Error: You did not enter a Task Name.')
    if y == '':
        messagebox.showerror('Error','Error: You did not enter a Task Description.')
    #if z == '':
    #    messagebox.showinfo('Error','Error: You did not enter a Date.')

    # check for valid date format
    validDate = False
    date_string = z
    date_format = '%m/%d/%Y'
    try:
        date = datetime.datetime.strptime(date_string, date_format)
        validDate = True
    except:
        messagebox.showerror('Error','Error: You did not enter a valid date.')

    # returns true/false for valid/invlaid inputs
    if x == '' or y == '' or z == '' or validDate == False:
        return False
    if x != '' and y != '' and z != '' and validDate != False:
        return True


# check if task is already in todolist 
def checkTaskName(x,y):
    if x in y:
        messagebox.showerror('Error','Error: That task already exists')
        return False
    if x not in y:
        return True
    

# check if date/time is already in todolist
def checkDateTime(x,y):
    if x in y:
        messagebox.showerror('Error','Error: There is already a task at that date and time.')
        return False
    if x not in y:
        return True
              

class ToDoList:
    def __init__(self):
        self.todoTasks = dict()

    # adds task to dictionary entry
    def addTask(self, newTaskName, newTask):     
        self.todoTasks[newTaskName] = newTask
        
    # displays all the dictionary entrys in a message box
    def displayTasks(self):     
        message = ''
        if bool(self.todoTasks) == False:
            messagebox.showinfo('List of Tasks','No tasks have been added.')
        else:
            for task, details in self.todoTasks.items():    
                message += f'{details.getType()} Task: {task} - {details.getDesc()}, occurs on {details.getDate()} at {details.getTime()}\n'
            messagebox.showinfo('List of Tasks',message)

    # removes a dictionary entry
    def removeTask(self, taskName):     
        del self.todoTasks[taskName]

    # creats a list of all tasks
    def listTasks(self):    
        taskList = []
        for task, details in self.todoTasks.items():
            taskList.append(f'{task}')
        return taskList
    
    # returns library for saving to pickle                            
    def returnTaskList(self):       
        return self.todoTasks

    # loads data into library from pickle
    def loadTaskList(self, data):
        self.todoTasks = data

    # lists task name keys in dictionary
    def taskNameList(self):
        taskList = list(self.todoTasks.keys())
        return taskList

    # list date/time for tasks in dictionay
    def taskDateTimeList(self):
        dateTimeList = []
        for task, details in self.todoTasks.items():
            dateTimeList.append(details.getDate()+details.getTime())
        return dateTimeList
            

class Task:
    def __init__(self, taskName, taskDesc, taskDate, taskTime):
        self.name = taskName
        self.desc = taskDesc
        self.date = taskDate
        self.time = taskTime
        self.type = 'Generic'

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getType(self):
        return self.type
        

class PersonalTask(Task):
    def __init__(self, taskName, taskDesc, taskDate, taskTime):
        super().__init__(taskName, taskDesc, taskDate, taskTime)
        self.type = 'Personal'


class SchoolTask(Task):
    def __init__(self, taskName, taskDesc, taskDate, taskTime):
        super().__init__(taskName, taskDesc, taskDate, taskTime)
        self.type = 'School'


class WorkTask(Task):
    def __init__(self, taskName, taskDesc, taskDate, taskTime):
        super().__init__(taskName, taskDesc, taskDate, taskTime)
        self.type = 'Work'


class RemoveTaskWindow:
    def __init__(self):
        try:
            self.win = tk.Toplevel()
            self.win.title('Remove Task')
            self.win.geometry('200x150')

            # delete task label and selection
            self.label = tk.Label(self.win, text = 'Select Task to Remove:')
            self.label.pack(pady=(10,0))
            self.select = ttk.Combobox(self.win, value = todolist.listTasks(), width=20)
            self.select.pack(pady=(10,0))
            self.select.current(0)
            
            # removes selected task
            self.remove = tk.Button(self.win, text='Remove', command = lambda:[todolist.removeTask(self.select.get()), messagebox.showinfo('Notification','Tast Deleted'), self.win.destroy()])
            self.remove.pack(pady=(10,0))

            # cancels remove
            self.cancel = tk.Button(self.win, text='Cancel', command = self.win.destroy)
            self.cancel.pack(pady=(10,0))
            
        except:
            self.win.destroy()
            messagebox.showerror('Error','No Tasks to Delete')
        

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-App')
        self.root.geometry('500x700')

        # app label
        self.appLabel = tk.Label(self.root, text = 'To-Do List Tracking App')
        self.appLabel.pack(pady=(10,0))

        # task name label and entry
        self.taskLabel = tk.Label(self.root, text='Task Name:')
        self.taskLabel.pack(pady=(10,0))
        self.entryName = tk.Entry(self.root, width=25)
        self.entryName.pack()

        # task description label and entry
        self.taskDesc = tk.Label(self.root, text='Description:')
        self.taskDesc.pack(pady=(10,0))
        self.entryDesc = tk.Entry(self.root, width=50)
        self.entryDesc.pack()

        # date entry
        self.date = tk.Label(self.root, text='Date (MM/DD/YYYY):')
        self.date.pack(pady=(10,0))
        self.entryDate = tk.Entry(self.root, width=25)
        self.entryDate.pack()

        # time entry
        self.time = tk.Label(self.root, text='Time:')
        self.time.pack(pady=(10,0))
        self.hour = tk.Scale(self.root, from_=0, to=23, resolution = 1, orient='horizontal', length=200, label='Hour')
        self.hour.pack()
        self.minute = tk.Scale(self.root, from_=0, to=55, resolution = 5, orient='horizontal', length=200, label='Minute')
        self.minute.pack()

        # task type selection
        self.type = tk.Label(self.root, text='Task Type:')
        self.type.pack(pady=(10,0))
        tasks = ['Generic', 'Personal', 'School', 'Work']
        self.taskType = ttk.Combobox(self.root, value = tasks)
        self.taskType.current(0)
        self.taskType.pack(pady=(10,0))

        # menu label
        self.menu = tk.Label(self.root, text = 'Menu:')
        self.menu.pack(pady=(30,0))
                
        # add task button
        self.add = tk.Button(self.root, text='Add Task', command = self.addTask)
        self.add.pack(pady=(10,0))

        # remove task button
        self.remove = tk.Button(self.root, text='Remove Task', command = self.removeTask)
        self.remove.pack(pady=(10,0))

        # display task button
        self.display = tk.Button(self.root, text='Display Tasks', command = self.displayTasks)
        self.display.pack(pady=(10,0))

        # quit program
        self.quit = tk.Button(self.root, text='Save and Quit', command = onQuit)
        self.quit.pack(pady=(10,0))

##        #display current info input in the data fields
##        self.displayInputs = tk.Label(self.root, text='Displays the current task being input into the To-Do App fields:')
##        self.displayInputs.pack(pady=(30,0))
##        self.displayButton = tk.Button(self.root, text='Display Inputs', command = self.currentInput)
##        self.displayButton.pack()

    # add task to task list    
    def addTask(self):

        isValid = checkFields(self.entryName.get(), self.entryDesc.get(), self.entryDate.get())     # check for valid input in data fields
        if isValid == True:

            value = todolist.taskNameList()     # check if task name is already in todolist
            isValid = checkTaskName(self.entryName.get(), value)
            if isValid == True:

                date = self.entryDate.get()     #check if date/time is already in todolist
                time = convTime(self.hour.get(), self.minute.get())
                value1 = date+time
                value2 = todolist.taskDateTimeList()
                isValid = checkDateTime(value1, value2)
                if isValid == True:
                     
                    if self.taskType.get()=='Generic':      # add a generic task
                        time = convTime(self.hour.get(), self.minute.get())
                        newTask = Task(self.entryName.get(), self.entryDesc.get(), self.entryDate.get(), time) # creats a new task using task class
                        todolist.addTask(self.entryName.get(), newTask)
                        message = f'The {self.taskType.get()} Task: {self.entryName.get()} - {self.entryDesc.get()} on {self.entryDate.get()} at {time} was added to your To-Do List.'
                        messagebox.showinfo('New Task Added',message)   # display confirmation message

                    if self.taskType.get()=='Personal':     # add a personal task
                        time = convTime(self.hour.get(), self.minute.get())
                        newTask = PersonalTask(self.entryName.get(), self.entryDesc.get(), self.entryDate.get(), time) # creats a new task using personal class
                        todolist.addTask(self.entryName.get(), newTask)
                        message = f'The {self.taskType.get()} Task: {self.entryName.get()} - {self.entryDesc.get()} on {self.entryDate.get()} at {time} was added to your To-Do List.'
                        messagebox.showinfo('New Task Added',message)   # display confirmation message
                            
                    if self.taskType.get()=='School':       # add a school task
                        time = convTime(self.hour.get(), self.minute.get())
                        newTask = SchoolTask(self.entryName.get(), self.entryDesc.get(), self.entryDate.get(), time) # creats a new task using school class
                        todolist.addTask(self.entryName.get(), newTask)
                        message = f'The {self.taskType.get()} Task: {self.entryName.get()} - {self.entryDesc.get()} on {self.entryDate.get()} at {time} was added to your To-Do List.'
                        messagebox.showinfo('New Task Added',message)   # display confirmation message

                    if self.taskType.get()=='Work':         #add a work task
                        time = convTime(self.hour.get(), self.minute.get())
                        newTask = WorkTask(self.entryName.get(), self.entryDesc.get(), self.entryDate.get(), time) # creats a new task using work class
                        todolist.addTask(self.entryName.get(), newTask)
                        message = f'The {self.taskType.get()} Task: {self.entryName.get()} - {self.entryDesc.get()} on {self.entryDate.get()} at {time} was added to your To-Do List.'
                        messagebox.showinfo('New Task Added',message)   # display confirmation message
            
                if isValid == False:
                    pass
            

    # delete task from task list
    def removeTask(self):
        self.removeTask = RemoveTaskWindow()
        self.removeTask.win.mainloop()      
          

    # diplay all tasks
    def displayTasks(self):
        todolist.displayTasks()


    # display currtent info input into data fields
    def currentInput(self):
        time = convTime(self.hour.get(), self.minute.get())    
        message = 'Task Name: ' + self.entryName.get() + ' | ' \
                  + 'Description: ' + self.entryDesc.get() + ' | ' \
                  + 'Date: ' + self.entryDate.get() + ' | ' \
                  + 'Time: ' + time + ' | ' \
                  + 'Type: ' + self.taskType.get()
        messagebox.showinfo('input',message)

    
# end the program
def onQuit():
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        file = open('todo.pickle','wb')
        data = todolist.returnTaskList()
        pickle.dump(data,file)
        file.close()
        root.destroy()


if __name__ == '__main__':
    todolist = ToDoList()

    try:
        file=open('todo.pickle','rb')
        data = pickle.load(file)
        todolist.loadTaskList(data)
        file.close()
    except:
        pass
        
    root = tk.Tk()
    app = ToDoApp(root)
    root.protocol('WM_DELETE_WINDOW', onQuit)
    root.mainloop()
