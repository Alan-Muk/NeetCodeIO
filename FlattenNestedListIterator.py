class NestedInteger:
	def isInteger(self) -> bool:


	def getInteger(self) -> int:


	def getList(self) -> [NestedInteger]:


class NestedIterator:
	def __init__(self, nestedList:[NestedInteger]):
		self.stack = []
		self.dfs(nestedList)
		self.stack.reverse()

	def next(self) -> int:
		return self.stack.pop()

	def hasNext(self) -> bool:
		return len(self.stack) > 0

	def dfs(self, nested):
		for n in nested:
			if n.isInteger():
				self.stack.append(n.getInteger())
			else:
				self.dfs(n.getList())