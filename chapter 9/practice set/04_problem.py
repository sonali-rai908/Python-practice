'''a file contains a word "Donkey" multiple times . you need to write  a program which replace this word with #### by updating the same file '''

with open("file.txt","r") as f:
    content=f.read() 

new_content=content.replace("Donkey" , "####")

with open("file.txt","w") as f:
         f.write(new_content)


print("Word replaced successfully")