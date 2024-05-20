class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def maximumSum(self, head:ListNode) -> int:
		slow, fast = head, head
		prev = None

		while fast and fast.next:
			fast = fast.next.next
			tmp = slow.next
			slow.nex = prev
			prev = slow
			slow = tmp

		res = 0
		while slow:
			res = max(res, prev.val + slow.val)
			prev = prev.next
			slow = slow.next

		return res



		
			