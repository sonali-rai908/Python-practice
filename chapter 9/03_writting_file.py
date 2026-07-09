st =" hey sonali, how are you?"

file=open("myfile.txt","w")

file.write(st)

file.close()

''' if the file which you mentioned in open()
  does not exist - pyhton creates it
  if exist - all old data is erased'''