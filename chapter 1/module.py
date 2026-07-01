# MODULE - module is a file containing code written by somebody else which can be imported and used in progams.
# its like a toolbox which contains all tools that makes  us easy to write our codes 

# PIP - it is like a module manager which helps to install modules as   "python -m pip intall pacakage_name "
# pahle ham "python -m pip --version "command ka use krke ye check karenge ki pip installed h ya nhi 
# agr installed h to konsa version hai 
# "python -m pip intall pacakge_name" command install krne ke liye module 
# "python -m pip list" command installed modules ki list check krne ke liye
# "python -m pip intall --upgrage pip" pip update krne ke liye 
# we can use the module by uing import keyword as import module name
# ctrl + / for multiple line comments 

# types of module -
# 1- built in modules - preintalled packages
# 2- extrenal modules - installed using pip 

import pyjokes
joke = pyjokes.get_joke()
print(joke)