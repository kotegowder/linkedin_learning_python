f=0
print(f)

# re-declaring the variable works
f="abc"
print(f)

# ERROR : variables of different types cannot be combined
#print("This is a string" + 123)
print("This is a string " + str(123))

# Global vs local variables in functions
def someFunction():
	#global f
	f="def"
	print(f)

someFunction()
print(f)

# Undefine variable run-time
#del f
#print(f)
