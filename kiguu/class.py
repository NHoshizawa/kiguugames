class Man:
	def __init__(self,name):
		self.name = name
		print("initialized!")
	def Hello(self):
		print("Hello "+self.name)
	def Goodbye(self):
		print("Goodbye "+self.name)
m=Man("David")
m.Hello()
m.Goodbye()