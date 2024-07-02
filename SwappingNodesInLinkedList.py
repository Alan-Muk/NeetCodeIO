class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def swapNodes(self, head:ListNode, k:int) -> ListNode:
		cur = head

		for i in range(k-1):
			cur = cur.next

		left = cur
		right = head
		while cur.next:
			cur.next 
			right = right.next

		left.val, right.val = right.val, left.val
		return head