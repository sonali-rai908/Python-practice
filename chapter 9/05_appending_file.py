string_to_add= "\nhey i am sonali there\n Nice to meet you"
file=open("myfile.txt","a")
file.write(string_to_add)
file.close()

''' if file exists then new data is added to at the end
     if doesnt exist python will create it
     existing data remains unchanged'''