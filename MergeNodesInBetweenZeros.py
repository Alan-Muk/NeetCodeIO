class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeNodes(self, head:ListNode) -> ListNode:
		curr = head
		dummy = ListNode()
		tail = dummy

		while curr.next:
			node = ListNode()
			while curr.next.val != 0:
				node.val += cur.next.val
				curr = curr.next
			tail.next = node
			tail = node.next
			curr = curr.next

		return dummy.next