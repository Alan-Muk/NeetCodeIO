class Solution:
	def validateStack(self, pushed:list[int], popped:list[int]) -> bool:
		stack = []

		i = 0
		for n in pushed:
			stack.append(n)
			while i < len(popped) and stack and popped[i] == stack[-1]:
				stack.pop()
				i += 1
		return not stack