# define a basic function
def func1():
	print("I am a function : func1")


# function that takes arguments
def func2(arg1, arg2):
	print(arg1, " ", arg2)	

# function that returns a value
def cube(x):
	return x*x*x

# function with defualt value for argument
def power(num, x=1):
	res = 1
	for i in range(x):
		res = res * num
	return res

# function with variables number of arguments
def multi_add(*args):
	res = 0
	for x in args:
		res = res + x
	return res

func1()
print(func1())
print(func1)	# funcionts them selves are objects - returns the object id
func2(10, 20)
print(func2(10, 20)) # function returns nothig - so you see None
print(cube(3))
print(power(2))
print(power(2, 3))
print(power(x=3, num=2)) # reversing the order - python interpreters maps when called with names
print(multi_add(10,4,5,10,4))
