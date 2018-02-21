from sys import *
import os

executable_name = argv[1][:-3]

os.system('python parser.py ' + executable_name + ".lc")
os.system('compile ' + executable_name)
os.remove(executable_name + ".cpp")
os.system(executable_name + ".exe")
