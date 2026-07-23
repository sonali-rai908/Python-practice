def main():
    try:
       a=int(input("Enter a number: "))
       print(a)

    except ValueError as e:
       print(e)

    finally:
        print("finally executed") 

main() 

# finally block will exceute at any cost ...it doesnt depends on whtehr try is sucessfull or not and whether the exception occurs or not
# it is mainly used in functions . when program is written under function