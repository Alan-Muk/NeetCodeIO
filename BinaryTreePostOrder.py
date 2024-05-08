class TreeNode:
	def __init__(self, left = None, right = None, val = 0):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def postOrder(self, root:TreeNode) -> list[int]:
		stack = [root]
		visit = [False]
		res = []

		while stack:
			cur, v = stack.pop(), visit.pop()

			if cur:
				if v:
					res.append(cur.val)
				else:
					stack.append(cur)
					visit.append(True)
					stack.append(cur.right)
					visit.append(False)
					stack.append(cur.left)
					visit.append(False)
		return res



			