# 🐍 Chapter 2 - Variables, Data Types, Input and Operators

## 📖 About This Chapter

In this chapter, I learned some of the fundamental concepts of Python that are used in almost every program.

The main topics covered in this chapter are:

1. Variables
2. Keywords and Identifiers
3. Data Types
4. `type()` Function
5. Type Casting
6. `input()` Function
7. Arithmetic Operators
8. Assignment Operators
9. Comparison Operators
10. Logical Operators
11. Practice Problems

These concepts helped me understand:

1. How Python stores data.
2. How different types of data are handled.
3. How to take input from users.
4. How to check and convert data types.
5. How to perform different operations on values and variables.

## 📦 Variables

1. A variable is a name that refers to a value stored in memory.
2. A variable can also be understood as a container used to store data.
3. Variables allow us to store values and use them later in a program.

**Example:**

    a = 3
    b = 8
    name = "Sonali"

Here:

a. `a` stores the value `3`.

b. `b` stores the value `8`.

c. `name` stores the value `"Sonali"`.

**Example:**

    a = 3
    b = 8
    c = "Sonali"

    print(a + b)
    print(c)

## 📝 Rules for Variable Names

1. A variable name can contain:
   a. Alphabets (`A-Z` and `a-z`)
   b. Digits (`0-9`)
   c. Underscores (`_`)

2. A variable name cannot start with a digit.

3. A variable name can start with:
   a. An alphabet
   b. An underscore (`_`)

4. Whitespace is not allowed in a variable name.

5. Variable names are case-sensitive.

**Example:**

    name
    Name
    NAME

All three are considered different variable names.

**Examples of valid variable names:**

    name = "Sonali"
    age_1 = 20
    _value = 10

**Examples of invalid variable names:**

    1name = "Sonali"      # Cannot start with a digit
    my name = "Sonali"    # Whitespace is not allowed

## 🔑 Keywords and Identifiers

### Keywords

1. Keywords are reserved words in Python.
2. They have special meanings and are used by Python for specific purposes.
3. Keywords cannot be used as variable names, function names, or other identifiers.

**Example:**

    if
    else
    True
    False
    None

### Identifiers

1. Identifiers are names used to identify different elements in a Python program.
2. Identifiers can be used for:
   a. Variables
   b. Functions
   c. Classes
   d. Modules

**Example:**

    name = "Sonali"

Here, `name` is an identifier.

## 🧩 Data Types

1. Data types tell Python what type of value a variable is storing.
2. Python automatically determines the data type based on the value assigned to a variable.

**Example:**

    a = "Sonali"  # String
    b = 55        # Integer
    c = 6.9       # Floating-point number
    d = True      # Boolean value
    e = None      # Represents the absence of a value

The basic data types learned in this chapter are:

1. `str`
   Used to store text or string values.

   **Example:**

       "Sonali"

2. `int`
   Used to store whole numbers.

   **Example:**

       55

3. `float`
   Used to store decimal numbers.

   **Example:**

       6.9

4. `bool`
   Used to store Boolean values.

   **Example:**

       True
       False

5. `NoneType`
   Represents the absence of a value.

   **Example:**

       None

## 💡 Python is Dynamically Typed

1. Python automatically determines the data type of a value.
2. We do not need to declare the data type of a variable before assigning a value to it.
3. The same variable can refer to values of different data types at different times.

**Example:**

    a = 10
    print(type(a))

    a = "Hello"
    print(type(a))

## 🔍 The type() Function

1. The `type()` function is used to check the data type of a value or variable.
2. It returns the type of the given object.

**Example:**

    a = 7

    print(type(a))

Output:

    <class 'int'>

## 🔄 Type Casting

1. Type casting is used to convert a value from one data type to another.
2. Some common type conversion functions are:
   a. `int()` - Converts a value to an integer.
   b. `float()` - Converts a value to a floating-point number.
   c. `str()` - Converts a value to a string.

**Example:**

    a = 7
    b = str(a)

    print(type(b))

Here, the integer value stored in `a` is converted into a string.

## ⌨️ Taking Input from the User

1. The `input()` function is used to take input from the user.
2. The text inside `input()` is displayed as a prompt to the user.
3. By default, `input()` returns the user's input as a string (`str`).

**Example:**

    name = input("Enter your name: ")

### Important Point

Even if the user enters a number, `input()` stores it as a string unless we convert it.

**Example:**

    a = input("Enter number 1: ")
    b = input("Enter number 2: ")

    print(a + b)

If the user enters:

    2
    4

The output will be:

    24

This happens because both values are strings, so the `+` operator concatenates them.

## 🔢 Taking Numeric Input

To perform mathematical operations, we need to convert user input into an appropriate numeric data type.

### Integer Input

**Example:**

    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))

    print(a + b)

If the user enters `2` and `4`, the output will be `6`.

### Decimal Input

**Example:**

    number = float(input("Enter a decimal number: "))

### Quick Summary

1. `input()` returns a string.
2. `int(input())` converts the input into an integer.
3. `float(input())` converts the input into a floating-point number.

## ➕ Operators in Python

1. Operators are symbols or keywords used to perform operations on values and variables.
2. Different operators are used for different types of operations.

### 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

1. `+` - Addition
2. `-` - Subtraction
3. `*` - Multiplication
4. `/` - Division
5. `%` - Modulus
6. `**` - Exponentiation
7. `//` - Floor Division

**Example:**

    a = 3
    b = 4

    print(a + b)
    print(a - b)
    print(a / b)
    print(a * b)

### 2. Assignment Operators

1. Assignment operators are used to assign values to variables.
2. They can also be used to update the existing value of a variable.

Common assignment operators:

1. `=`
2. `+=`
3. `-=`
4. `*=`
5. `/=`

**Example:**

    c = 4 - 3

    print(c)

The result of `4 - 3` is assigned to `c`.

**Example of updating a variable:**

    d = 5

    d += 3
    print(d)

This is equivalent to:

    d = d + 3

Similarly:

    d -= 2

is equivalent to:

    d = d - 2

### 3. Comparison Operators

1. Comparison operators are used to compare two values.
2. The result of a comparison is a Boolean value: `True` or `False`.

Common comparison operators:

1. `==` - Equal to
2. `!=` - Not equal to
3. `>` - Greater than
4. `<` - Less than
5. `>=` - Greater than or equal to
6. `<=` - Less than or equal to

**Example:**

    a = 7
    b = 6

    print(a == b)
    print(a <= b)
    print(a >= b)

### 4. Logical Operators

1. Logical operators are used to combine or modify conditions.
2. The main logical operators are `and`, `or`, and `not`.

#### and

1. Returns `True` only when both conditions are `True`.

**Example:**

    True and True

Result:

    True

#### or

1. Returns `True` when at least one condition is `True`.

**Example:**

    True or False

Result:

    True

#### not

1. Reverses a Boolean value.
2. `True` becomes `False`, and `False` becomes `True`.

**Example:**

    not True

Result:

    False

## 📝 Practice Problems

The practice problems in this chapter helped me apply the concepts learned above.

The problems focused on:

1. Working with variables.
2. Performing arithmetic operations.
3. Taking input from the user.
4. Working with strings and numbers.
5. Checking data types using `type()`.
6. Converting values using type casting.
7. Using different operators.

## 🧠 Key Things I Learned

1. Variables are used to store values that can be used later in a program.
2. Python automatically determines the data type of a value.
3. Python is dynamically typed.
4. `type()` is used to check the data type of a value or variable.
5. Type casting is used to convert values from one data type to another.
6. `input()` returns user input as a string by default.
7. `int(input())` can be used to take integer input.
8. `float(input())` can be used to take decimal input.
9. Operators are used to perform different operations on values and variables.
10. Comparison operations return Boolean values: `True` or `False`.
11. Logical operators are used to combine or modify conditions.

## 🎯 Chapter Takeaway

1. This chapter helped me understand how Python handles data.
2. Most Python programs work with values that need to be stored, processed, and sometimes taken as input from the user.
3. Understanding variables, data types, input, type conversion, and operators is important before moving to more advanced Python concepts.

A basic Python program can often follow this flow:

    Take Input
        ↓
    Store Data in Variables
        ↓
    Check or Convert Data Types
        ↓
    Perform Operations
        ↓
    Display Output

## 🐍 Learning Journey

This chapter is part of my Python learning journey, where I am learning concepts step by step and practicing them through code and small problems.

Topics covered in this chapter:

Variables, Keywords, Identifiers, Data Types, `type()`, Type Casting, `input()`, Arithmetic Operators, Assignment Operators, Comparison Operators, Logical Operators, and Practice Problems.