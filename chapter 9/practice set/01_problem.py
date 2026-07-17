#  Write a program tp read the text from a given file "poems.txt" and find out whether it contains the word "twinkle"

file=open("poems.txt","r")
poem=file.read()
print(poem)

if "twinkle" in poem:
    print("Yes , word twinkle is present in the poem")
else:
    print("No , word twinkle is not present in the poem")

file.close()