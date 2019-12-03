#Jessie Fehrenbach
# CSCI 101 section G
# Create project
import os

username = []

#print("Welcome to note manager! to get started enter your username.")
#username += input('USERNAME>')
print("use funtion 'new_class('class name')' to create a new class directory")
print("enter 'help()' for all the funtions")
def help():
    print('.'*70)
    print('save_notes() : takes input notes and saves it to your class directory')
    print('new_class("name") : creates a new directory for you to save class notes to')
    print('open_notes() : changes to your desired notes directory and opens one of your notes files')
    print('.' *70)

def save_notes():
    #print('enter your class directory')
    #directory = input('directory>' )
    #current = os.getcwd()
    #current.split("\")
    #if current[-1] != directory:
    #    os.chdir(directory)
    print('Enter the title of your notes')
    title = input('NOTES>')
    with open('notes.txt','a') as save:
        save.write(title + ',')
    with open(title + '.txt', 'a') as f:
        print('enter your class notes using new line')
        notes = input('NOTES>')
        f.write(notes)
def open_notes():
    directory = input('input the title of your class> ')
    os.chdir(directory)
    print(os.getcwd())
    file = input('input the title of your notes with .txt> ')
    with open(file, 'r') as f:
        print('.'*70)
        print(f.read())
        print('.'*70)

def find_notes():
    print('enter key words you had in your notes')
    key = input('KEY> ')
    s = '.txt'
    with open('classes.txt','r') as f:
        exist = False
        contents = f.read()
        contents = contents.split(',')
        contents.pop()
        for i in contents:
            os.chdir(i)
            with open('notes.txt', 'r') as notes: # save notes into a .txt in the working direcotry,,, Check
                class_notes = notes.read()
                class_notes = [x for x in class_notes.split(',') if x]
  #              class_notes = class_notes.split(',')

                for r in class_notes:
                    notes_file = r + '.txt'
                    print(notes_file)
                    with open(notes_file, 'r') as stinkey:
                        real = stinkey.read()
                        if key in real:
                            file = os.getcwd()
                            file = file.split('\\')
                            exist = True
                            file_name = r + '.txt'
                reverse_dir()
        if exist == True:
            print('The notes are in:', file[-1] )# print the directory
            print('The title of the notes are ', file_name)
        else:
            print('Notes could not be found')    
        
     #   for directory in 
    
def reverse_dir():
    cwd = str(os.getcwd())
    cwd = cwd.split('\\')
    os.chdir('..')
    return cwd[-2]
    


def new_class(name): # add area where if it exits promt them
    try:
        os.mkdir(name)
    except OSError:
        print('Class directory',name,'failed')
    else:
        print('successfully made directory',name)
        with open('classes.txt', 'a') as f:
            f.write(name + ',')
        os.chdir(name)
        print('moving to directory', name)
        print(os.getcwd())
        print('would you like to save notes to this directory? [Y/N]')
        answer = input('>>>')
        if answer == 'Y':
            save_notes()
            reverse_dir()
        else:
            print('input error')
            print("use funtion 'new_class(<class name>)' to create a new class directory")
            
    
    
