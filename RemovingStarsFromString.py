class Solution:
	def removeStar(self, s:str) -> str:
		stack = []

		for c in s:
			if c == "*":
				stack and stack.pop()

			else:
				stack.append(c)

		return "".join(stack)
