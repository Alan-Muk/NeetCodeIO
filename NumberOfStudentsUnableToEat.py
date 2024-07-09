class Solution:
	def countStudents(self, students:list[int], sandwiches:list[int]) -> list[int]:
		res = len(students)
		count = Counter(students)

		for s in sandwiches:
			if count[s] > 0:
				count[s] -= 1
				res -= 1
			else:
				return res

		return res