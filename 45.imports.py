import sys
import imports_sample45 # Interpreter will look for sample module based on the list sys.path, starting with 0th place and so on
'''
from sample import print_Sample 
# Can import class/method/variables from module
'''

print(sys.path) # Gives list of paths where interpreter will look for modules.
imports_sample45.print_Sample("happy") # Good practice to use filename.method or filename.variable while importing. p