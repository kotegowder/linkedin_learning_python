class myClass():
	def method1(self):
		print("myClass method1")

	def method2(self, someStr):
		print("myClass method2 " + someStr)

class myAnotherClass(myClass):
	def method1(self):
		myClass.method1(self)
		print("myAnotherClass method1")

	def method2(self, someStr):
		print("myAnotherClass method2")

def main():
	c = myClass()

	c.method1()
	c.method2("This is a string")

	c1 = myAnotherClass()
	c1.method1()
	c1.method2("This is a string")

if __name__ == "__main__":
	main()

