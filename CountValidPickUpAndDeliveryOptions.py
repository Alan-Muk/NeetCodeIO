class Solution:
	def countOrders(self, n:int) -> int:
		slots = 2 * n
		output = 1

		while slots  > 0:
			valis_choices =  slots * (slots - 1) // 2
			output *= valis_choices
			slots -= 2
		return output % (10**9 + 7)