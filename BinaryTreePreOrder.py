class TreeNode:
	def __init__(self, left = None, right =None, val = 0):
		self.left = left
		self.right = right
		self.val = val

class Soutuion:
	def preOrder(self, root:TreeNode) -> list[int]:

		cur, stack = root, []
		res = []

		while cur or stack:
			if cur:
				res.append(cur.val)
				stack.append(cur.right)
				cur = cur.left
			else:
				cur = stack.pop()

		return res