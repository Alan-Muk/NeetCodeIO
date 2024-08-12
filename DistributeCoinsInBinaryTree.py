class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.right = right
		self.left = left

class Solution:
	def distributeCoins(self, root:TreeNode) -> int:
		self.res = 0

		def dfs(cur):
			if not root: return [0, 0]

			l_size, l_coins =  dfs(cur.left)
			r_size, r_coins =  dfs(cur.right)

			size = 1 + l_size + r_size
			coins = cur.val + l_coins + r_coins
			self.res += abs(size - coins)
			return [size, coins]

		dfs(root)
		return self.res