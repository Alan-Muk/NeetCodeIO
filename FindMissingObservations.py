class Solution:
	def missingRolls(self, rolls:list[int], mean:int, n:int) -> list[int]:
		m = len(rolls)
		total_sum = mean * (m + n)
		missing_sum = total_sum - sum(rolls)


		if missing_sum > n * 6 or missing_sum < n:
			return []

		res = []

		while n:
			dice = min(6, missing_sum - n + 1)
			res.append(dice)
			missing_sum -= dice
			n -= 1

		return res