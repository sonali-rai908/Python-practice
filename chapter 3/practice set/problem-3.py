#write a program to detect double space in astring 
a= "Sonali is a  girl"
print(a.find("  ")) # it will retirn the index position of double space is present but is not present then it will return -1 
 
 # now replacing the double space by simgle space in a 
print(a.replace("  "," "))

print(a) # it will print the  original string without any change . thats why strings are called immutable which means that you cannot change them by running functions on them
