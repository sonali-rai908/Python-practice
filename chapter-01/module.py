# 📦 MODULES & PIP — Python Notes

# MODULE
# A module is a Python file containing reusable code.
# We can import and use it in our programs.

# Module can be understood as a toolbox containing useful tools/functions
# that make writing programs easier.

# Importing a module:
# import module_name


# PIP
# PIP is a package manager used to install and manage external packages.

# Check whether pip is installed and see its version:
# python -m pip --version

# Install a package:
# python -m pip install package_name

# Check installed packages:
# python -m pip list

# Upgrade pip:
# python -m pip install --upgrade pip


# TYPES OF MODULES

# 1. Built-in Modules
# These come pre-installed with Python.

# 2. External Modules
# These are usually installed using pip before we can use them.


# SHORTCUT
# Ctrl + / → Comment or uncomment multiple lines

import pyjokes
joke = pyjokes.get_joke()
print(joke)