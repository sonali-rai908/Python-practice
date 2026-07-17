''' to find out whether a file is idential and matches the content of another file'''

with open("this.txt") as f:
    content =f.read()

with open("this_copy.txt") as f:
    new_content=f.read()

if (content == new_content):
    print("Both files are identical")

else:
    print("no,files are not same")