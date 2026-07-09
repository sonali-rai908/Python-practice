file = open("file.txt")   # read is a deafult mode , if you not mention anything it will open in read mode
data = file.read()
print(data)
file.close()

#if file doesnot exist -- FileNotFoudError