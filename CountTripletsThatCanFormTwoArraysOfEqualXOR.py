class Solution:
	def countTriplets(self, arr:list[int]) -> int:
		N = len(arr)
		res = 0

		prefix = 0
		prev_xor_count = defaultdict(int)
		prev_xor_count[0] = 1
		prev_xor_index_sum = defaultdict(int)

		for i in range(N):
			prefix ^= arr[i]

			if prev_xor_count[prefix]:
				res += i * prev_xor_count[prefix] - prev_xor_index_sum[prefix]

			prev_xor_count[prefix] += 1
			prev_xor_index_sum[prefix] += i + 1


		return res