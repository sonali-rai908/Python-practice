#It makes code easier to understand and helps IDEs (like VS Code) catch mistakes.
# ==========================
# Type Hints in Python
# ==========================

# 1. Variable Type Hints
age: int = 20
name: str = "Sonali"
height: float = 5.6
is_student: bool = True

print("Variable Type Hints")
print("Age:", age)
print("Name:", name)
print("Height:", height)
print("Is Student:", is_student)


# --------------------------
# 2. Function with int return type
# --------------------------
def add(a: int, b: int) -> int:
    return a + b


print("\nFunction Returning int")
print("Sum:", add(10, 20))


# --------------------------
# 3. Function with string return type
# --------------------------
def greet(person: str) -> str:
    return f"Hello, {person}!"


print("\nFunction Returning str")
print(greet("Sonali"))


# --------------------------
# 4. Function returning None
# --------------------------
def display(message: str) -> None:
    print(message)


print("\nFunction Returning None")
display("Welcome to Python Type Hints!")


# --------------------------
# 5. List Type Hint
# --------------------------
numbers: list[int] = [10, 20, 30, 40, 50]
names: list[str] = ["Aman", "Priya", "Rahul"]

print("\nList Type Hint")
print("Numbers:", numbers)
print("Names:", names)


# --------------------------
# 6. Dictionary Type Hint
# --------------------------
marks: dict[str, int] = {
    "Math": 95,
    "Science": 90,
    "English": 88
}

print("\nDictionary Type Hint")
print(marks)


# --------------------------
# 7. Tuple Type Hint
# --------------------------
point: tuple[int, int] = (15, 25)

print("\nTuple Type Hint")
print(point)


# --------------------------
# 8. Set Type Hint
# --------------------------
colors: set[str] = {"Red", "Blue", "Green"}

print("\nSet Type Hint")
print(colors)

