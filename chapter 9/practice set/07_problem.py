''' write a program to find out that in which line python is presnt in ques 6 '''


with open("log.txt", "r") as f:
   lines =f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes pyhton is present in line number {lineno}")
        break
    line+=1

else:
    print("No python is not present")