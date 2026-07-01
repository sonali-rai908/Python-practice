# write aprogram to create a dictionary of hindi words with values as their english translation.Provide user with an option to look it up
dictionary={
    "madad":"HELP",
    "billi":"CAT",
    "kitab":"BOOK",
    "kursi":"CHAIR",
    "darwaza":"DOOR"
}
word=input("Enter the word you want the meaning of :")
if word in dictionary:
    print(dictionary[word])
else:
    print("This word is not in our dictionary.")