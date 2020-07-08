# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.stack=[]
		self.minMax=[]
		
    def peek(self):
        return self.stack[-1]

    def pop(self):
		self.minMax.pop()
		return self.stack.pop()

    def push(self, number):
        thisMinMax={"min":number,"max":number}
		if len(self.minMax)>0:
			thisMinMax["min"]=min(thisMinMax["min"],self.getMin())
			thisMinMax["max"]=max(thisMinMax["max"],self.getMax())
		self.minMax.append(thisMinMax)
		self.stack.append(number)
			
    def getMin(self):
        val=self.minMax[-1]
		return val["min"]

    def getMax(self):
        val=self.minMax[-1]
		return val["max"]
