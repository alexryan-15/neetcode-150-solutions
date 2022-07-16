# This solution is adding two numbers that are represented in the form of linked lists.
# As long as one of the lists or a carry value exists, the values to be added are determined
# based on what is available, then those numbers are added. Then, the next node is made
# with the required value. The pointers for the next number are then updated.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    	dummy = ListNode()
    	cur = dummy

    	carry = 0
    	while l1 or l2 or carry:
    		v1 = l1.val if l1 else 0
    		v2 = l2.val if l2 else 0

			val = v1 + v2 + carry
			carry = val // 10
			val = val % 10
			cur.next = ListNode(val)

			cur = cur.next
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None

		return dummy.next
