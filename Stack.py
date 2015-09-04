class Stack:
	def __init__(self):
		self.stack = []
	
	def checkSize(self):
		if len(self.stack) == 0: 		
			return 0
		else:
			return len(self.stack)
	def pop(self):
		return self.stack.pop()
	def push(self, item):
		self.stack.append(item)
