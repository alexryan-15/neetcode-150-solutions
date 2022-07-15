# This solution uses two pointers with a gap of n. Both start at the head, and the right pointer
# is moved until it is at the end of the list. Since there is a gap of n in between, the left
# pointer is at the nth node from the end of the list. Then, the next node from the left pointer
# is removed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		dummy = ListNode(0, head)
		left = dummy
		right = head

		while n > 0:
			right = right.next
			n -= 1

		while right:
			left = left.next
			right = right.next

		left.next = left.next.next
		return dummy.next
