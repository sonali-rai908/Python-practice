# a spam comment is defined as a text containing folowing keywords
# "make a lot of money","buy now","subscribe this","click this". Write a program to detect these spams 
spam_keywords=["make a lot of money","buy now","subscribe this","click this"]

message=input("Enter your comment:")

if (message in spam_keywords):
    print("You received a spam message.\nBe carefull with this messages.")

else:
    print("Your messgae is not a spam .\nYou are safe.")     

# the program which ihad written is not so  effective because whwn i had written message in spam_keyword 
#it will check for the whole messge means if you write "buy now" which completely matchs tha keyword the it 
#will show that it is spam but i wll write "nice video,please click this" it will not considered as spam 
# whether it contains te spamkeyword 
# so the correct programwill be
 
k1="make a lot of money"
k2="buy now"
k3="subscribe this"
k4="click this"

message=input("Enter the comment:").lower()

if ((k1 in message) or (k2 in message) or (k3 in message) or (k4 in message) ):
    print("You received a spam message.\n Needed to be safe.")

else:
    print("Your message is not spam.\nYou are safe")    

#THIS IS CORRECT PROGRAM    