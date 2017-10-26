class BinaryTree:
	def __init__(self, root):
		self.left = None
		self.right = None
		self.root = root
		self.size = 1

	def insert(self, Node):
		temp = self.root
		if Node.data > self.root.data:
			while temp.right != None:
				temp = temp.right
			temp.right = Node
		else:
			while temp.left != None:
				temp = temp.left
			temp.left = Node
		self.size = self.size + 1

	def printInOrder(self, Node):
		if Node == None:
			return 
		self.printInOrder(Node.left)
		print(Node.data)
		self.printInOrder(Node.right)



class TreeNode:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.parent = None
		self.data = data


def main():
	temp = TreeNode(10)
	left = TreeNode(5)
	right = TreeNode(15)
	rightmost = TreeNode(20)
	myTree = BinaryTree(temp)
	myTree.insert(left)
	myTree.insert(right)
	myTree.insert(rightmost)
	myTree.printInOrder(myTree.root)
	

if __name__ == "__main__": main()



