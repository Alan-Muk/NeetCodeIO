class Solution:
	def finalPrice(self, prices:list[int]) -> list[int]:
		
		res = [p for p in prices]

		stack = [] #index, values

		for i in range(len(prices)):
			while stack and prices[stack[-1]] >= prices[i]:
				j = stack.pop()
				res[j] -= prices[i]
			stack.append(i)

		return res