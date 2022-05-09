import ListNode
class LinkList:
	def __init__(self, head=None):
		self.head = head


	def search_list(head: ListNode, key: object) -> ListNode:
		while head and head.val != key:
			head = head.next
		return head  #None if not found

	def insert_after(node: ListNode, new_node: ListNode): 
		node.next, new_node.next = new_node, node.next 

	def delete_after(node: ListNode):
		node.next = node.next.next 