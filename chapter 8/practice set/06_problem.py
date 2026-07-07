# covert inches to cm
def inch_to_cm(inch):
    cm=inch*2.54
    return cm

inch=float(input("Enter the value in inch: "))

cm = inch_to_cm(inch)  

print(f"{inch} inches = {cm} cm")  