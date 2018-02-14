#!/urs/bin/python
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
		
class VideoObj(object):
	name = ""
	finished = False
	def __init__(self, timestamp, status):
		self.name = timestamp
		self.finished = status
		

		
		
q = Queue()

q.enqueue(VideoObj("v1",False))
temp = q.dequeue()
print(temp.name + " - " + str(temp.finished))

#print(q.size())
#print(q.isEmpty())
#print("Fjerner: ",q.dequeue())