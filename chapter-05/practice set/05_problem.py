# create an empty dictionary . allow 4 freinds to enter their favourite language s value and use key as teir names . assume that the names are unique 
d={}
for freind in range(4):
    name=input("Enter your name :")
    lang=input("Enter your favourite language:")
    # d.update({name:lang})
    d[name]=lang  # if we write the same name two or three times then the last one mentiined will be writte i dictionary 
print(d)