class Solution:
	def kthDistinct(self, arr:list[str], k:int) -> str:

		# for i in range(len(arr)):
		# 	distinct_flag = True
		# 	for j in range(len(arr)):
		# 		if i == j:
		# 			continue
				
		# 		if arr[i] == arr[j]:
		# 			distinct_flag = False
		# 			break

		# 	if distinct_flag:
		# 		k -= 1
		# 		if k == 0:
		# 			return arr[i]

		# return ""
		count = defaultdict(int)

		for s in arr:
			count[s] += 1

		for s in arr:
			if count[s] == 1:
				k -= 1

			if k == 0:
				return s

		return ""