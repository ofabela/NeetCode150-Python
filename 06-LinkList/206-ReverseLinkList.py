import ListNode
class Solution:
	def reverseList(self, head):
		curr, prev = head, None	
		while curr:
			next, curr.next = curr.next, prev
			curr, prev = next, curr
		return prev
