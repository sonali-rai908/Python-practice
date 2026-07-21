# write a program to display a/b where a nd b are integers . if b=  , display infinite by handling the "ZeroDivisionError"
while True:
    try:
      a = int(input("Enter the value of a: "))
      b = int(input("Enter the value of b: "))

      print("Result: " ,a/b)
      break

    except ValueError:
      print("Please enter only integers.")

    except ZeroDivisionError:
      print("Infinite")
      
         

    except Exception as e:
       print("Something went wrong: ",e)
       
print("Thank u")