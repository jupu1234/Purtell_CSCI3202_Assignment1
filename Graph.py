
class Graph:
	
	def __init__(self):
		self.graph = {}

	def addVertex(self, value):
		if value in self.graph:
			print "Vertex already exists"
		else:
			self.graph[value] = []
	
	def addEdge(self, value1, value2):
		if value1 and value2 in	self.graph:						
			if value2 not in self.graph[value1]:				
				self.graph[value1].append(value2)		
			if value1 not in self.graph[value2]:
				self.graph[value2].append(value1)
		else:
			print "One or more vertices not found"
	
	def findVertex(self, value):
		if value in self.graph:
			print self.graph[value]
	
	def __retr__(self):        
		return self
	
	def __getitem__ (self, key):
		return self.graph[key]




