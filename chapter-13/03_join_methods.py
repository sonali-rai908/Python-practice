# join() ka use list, tuple ya kisi iterable ke elements ko ek string me jodne ke liye hota hai.
# syntax : separator.join(iterable)

names = ["sonali","riya","ankit"]

result = " ".join(names)  # space se join krega
final = "::".join(names)
print(final)
print(result)

letters = ["P", "Y", "T", "H", "O", "N"]

result = "".join(letters)

print(result)

# it only works for strings , if you make a list of numbers then you have to convert it into string first
numbers = [1, 2, 3]

result = ",".join(map(str, numbers))

print(result)

