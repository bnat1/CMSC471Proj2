from math import *
import sys

dims = 2
__counter = 0
def my_func(x, y):
	global __counter
	__counter += 1
	if(__counter > 800):
		sys.exit(0)
	return x + y