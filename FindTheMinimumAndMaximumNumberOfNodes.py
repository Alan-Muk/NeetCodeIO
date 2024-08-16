class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def nodesBetweenCriticalPoint(self, head:ListNode) -> list[int]:

		def critical(prev, curr, nxt):
			return (prev.val > curr.val < nxt.val or 
					prev.val < curr.val > nxt.val)

		prev, curr = head, head.next
		nxt = cur.next
		min_dist, max_dist = float("inf"), -1

		prev_crit_index = 0
		first_crit_index = 0
		i = 1 # index of cur

		while nxt:
			if critical(prev, curr, nxt):
				if first_crit_index:
					max_dist = i - first_crit_index
					min_dist = min(min_dist, i - prev_crit_index)
				else:
					first_crit_index = i
				prev_crit_index = i

			prev, curr, nxt = curr, nxt, nxt.next
			i += 1

		if min_dist == float("inf"):
			min_dist = -1


		return [min_dist, max_dist]