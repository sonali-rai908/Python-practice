'''repeat program 4 for a list of such words to be censored'''
words={"Donkey","Lion","tiger","Tiger"}

with open("file.txt","r") as f:
    content=f.read()

for word in words:
    new_content=content.replace(word , "#"*len(word))
    with open("file.txt","w") as f:
     f.write(new_content)

        