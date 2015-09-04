from Graph import *
from random import randint
#Queue
#Creates and tests Queue of 10 integers. Implements FIFO 0 goes in  #first then 1 up to 9. 0 comes out first then 9 last
sizeofqueue = 10
i = 0;
queue = Queue.Queue(sizeofqueue)
while i < sizeofqueue:
	queue.put(i)
	i += 1
print "testing queue"
while queue.empty() != True:		
	print queue.get();
print " "

#Stack
#Creates a stack and tests a stack of 10 integers. Implements LIFO 0 goes in first up to 9 then nine comes out first
sizeofstack = 10
i = 0;
stack = Stack()
while i < sizeofstack:
	stack.push(i)
	i += 1
print "testing stack"
while stack.checkSize() != 0:
	print stack.pop()
print " "

#Graph
#creates a Graph intially with 10 unconnected nodes then randomly connects the nodes
#then randomly searches for 5 nodes
graph = Graph()
i = 0
while i < 10:
	graph.addVertex(i)
	i += 1
i = 0
while i < 20:
	graph.addEdge(randint(0,9), randint(0,9))
	i += 1
i = 0
while i < 5:
	graph.findVertex(randint(0,10))
	i += 1


