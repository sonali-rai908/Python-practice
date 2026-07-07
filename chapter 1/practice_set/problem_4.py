# write a python program to print the contents of a directory using the os module . Search online for the function which does that
import os

#specify the directory you want to list 
directory_path ='/'

# list all files and diretcories in the specified path
contents = os.listdir(directory_path)

#print each file and directory name
for items in contents:
    print(items)