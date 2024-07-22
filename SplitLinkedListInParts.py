class ListNode:
	def __init__(self, next=None, val = 0):
		self.next = next
		self.val = val

class Solution:
	def splitListToParts(self, head:ListNode, k:int) -> list[ListNode]:
		length, curr = 0, head

		while curr:
			curr = curr.next
			length += 1

		base_len, remainder = length // k, length % k

		curr = head
		res = []
		for i in range(k):
			res.append(curr)
			for j in range(base_len - 1 + (1 if remainder else 0)):
				if not curr.next:
					break
				curr = curr.next
			remainder -= (1 if remainder else 0)
			if curr:
				curr.next. curr = None, curr.next

		return res