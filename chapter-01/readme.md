# Chapter 01 – Getting Started with Python 🐍

## 📚 What I Learned

### 1. My First Python Program
- Wrote my first Python program using the `print()` function.
- Learned how Python executes code line by line.
- Ran Python files using the terminal.

Example:
```python
print("Hello, World!")
```

---

### 2. Python as a Calculator
Python can be used as a calculator to perform arithmetic operations.

Example:
```python
print(5 + 3)
print(10 - 2)
print(4 * 5)
print(20 / 4)
```

---

### 3. REPL (Python Interactive Shell)
**REPL** stands for:
- **R** – Read
- **E** – Evaluate
- **P** – Print
- **L** – Loop

It allows us to write and execute Python code one line at a time without creating a `.py` file.

### How to Open the REPL
Open Command Prompt (or PowerShell) and type:

```bash
python
```

or

```bash
py
```

If Python is installed correctly, you'll see something like:

```text
>>>
```

This `>>>` prompt means the Python REPL is ready.

To exit the REPL:

```python
exit()
```

or press:

```
Ctrl + Z
Enter
```
(Windows)

---

### 4. Modules in Python
A **module** is a file that contains reusable Python code.

We can install external modules using **pip**.

Example:

```bash
pip install pyjokes
```

Import and use:

```python
import pyjokes

print(pyjokes.get_joke())
```

---

### 5. What is pip?
`pip` is Python's package manager.

It is used to install, update, and remove Python packages.

Common commands:

```bash
pip install module_name
```

```bash
pip uninstall module_name
```

```bash
pip list
```

---

## ⚠️ Problem I Faced

### Error
Initially, this command didn't work:

```bash
pip install module_name
```

### Temporary Solution

I used:

```bash
python -m pip install module_name
```

This worked because it directly used Python's pip module.

---

### Permanent Solution

The `pip` folder was not added to the **System PATH**.

After adding Python and the **Scripts** folder to the PATH environment variable, I could simply use:

```bash
pip install module_name
```

without writing:

```bash
python -m pip
```

---

## 📌 Key Takeaways

- Installed Python successfully.
- Wrote my first Python program.
- Used Python as a basic calculator.
- Learned about the Python REPL and how to open it.
- Understood what modules are.
- Learned how to install modules using `pip`.
- Solved the `pip` command not recognized issue by using `python -m pip` and later fixing the PATH variable.

---

## 🚀 Chapter Summary

This chapter introduced the fundamentals of Python, including writing the first program, using Python as a calculator, understanding the REPL, installing external modules with `pip`, and resolving a common `pip` PATH issue. It provided the foundation required for future Python development.