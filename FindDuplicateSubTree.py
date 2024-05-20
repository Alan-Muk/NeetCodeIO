class TreeNode:
	def __init__(self, left=None, right=None, val=0):
		self.left = left
		self.right = right
		self.val = val

class Solution:
	def findSubTree(self, root:TreeNode) -> TreeNode:
		subtrees = defaultdict(list)

		def dfs(node):
			if not node:
				return "null"
			s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
			if len (subtrees[s]) == 1:
				res.append(node)
			subtrees[s].append(node)
			return s


		res = []
		dfs(root)
		return res
