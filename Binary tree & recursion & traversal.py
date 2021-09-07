"""
Binary tree & recursion & traversal
Source: PKU 李晓明 weibo
"""
class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class BinaryTree:
	def __init__(self):
		self.head = None

	def create(self, triple):
		root = None
		if triple:
			root = TreeNode(triple[0], None, None)
			if self.head == None:
				self.head = root
			root.left = self.create(triple[1])
			root.right = self.create(triple[2])
		return root

	def preroot_traversal(self, root):
		if root == None:
			return
		else:
			print(root.data, end=' ')
			self.preroot_traversal(root.left)
			self.preroot_traversal(root.right)
		return

	def midroot_traversal(self, root):
		if root == None:
			return
		else: 
			self.midroot_traversal(root.left)
			print(root.data, end=' ')
			self.midroot_traversal(root.right)
		return

	def postroot_traversal(self, root):
		if root == None:
			return
		else:
			self.postroot_traversal(root.left)
			self.postroot_traversal(root.right)
			print(root.data, end=' ')
		return

t = BinaryTree()
tree = (1,(2,(4,(),(7,(),())),()),(3,(5,(),()),(6,(),())))
t.create(tree)
print()
t.preroot_traversal(t.head)
print()
t.midroot_traversal(t.head)
print()
t.postroot_traversal(t.head)
print()




