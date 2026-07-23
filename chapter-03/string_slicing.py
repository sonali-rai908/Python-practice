name = "sonali"
length=len(name)
print("length of the string is :", length)
character1 = name[0]
print(character1) # outout will be s as indexing starts form 0 from forward 
print(name[-1]) # output will be i as indexing starts from -1 from backward and termed as negative indexing 

sliced_name=name[0:3] # output will be son as 3 is not included 
print(sliced_name)

print(name[:4]) # output willl be sona . it is same as [0:4]
print(name[1:]) # outout will be onali. it is sae as [1:5]

sliced_part=name[-4:-1]
print(sliced_part)

# skip slicing concept
print(name[0:4:2]) #it will slice the string by skipping letters 
                    # it will start from 0 index and run till index 4 with skipping aletter between them . it will take second letter after every entry .
                    # as here output will be sn means s at 0 index then second letter after it is n then l but l is at 4 index so it will not be included
                     