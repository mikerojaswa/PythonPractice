class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class UnorderedList:
	def __init__(self):
		self.head = None
		self.size = 0
    
	def isEmpty(self):
		return self.head == None

	def add(self, Node):
		Node.next = self.head
		self.head = Node
		self.size = self.size + 1

	def printList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next

	def remove(self, data):
		current = self.head
		#case that the node to be deleted is at the very begining
		if current.data == data:
			self.head = current.next
			return
		previous = self.head
		current = current.next
		while current != None:
			if current.data == data:
				previous.next = current.next
				return
			else:
				current = current.next
				previous = previous.next




def main():
	temp = Node(1)
	temp2 = Node(2)
	temp3 = Node(3)
	mylist = UnorderedList()
	mylist.add(temp)
	mylist.add(temp2)
	mylist.add(temp3)
	mylist.remove(1)
	mylist.printList()	

if __name__ == "__main__": main()
