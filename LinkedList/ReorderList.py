# This solution first finds the middle of the list, which will be needed so that each half
# can be dealt with individually. Then, the second half of the list is reversed as one would
# do to a normal list with a temp variable. Then, both of the halves are merged in place to
# achieve the final ordering of the list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
		slow, fast = head, head.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		second = slow.next
		prev = slow.next = None
		while second:
			tmp = second.next
			second.next = prev
			prev = second
			second = tmp

		first, second = head, prev
		while second:
			tmp1, tmp2 = first.next, second.next
			first.next = second
			second.next = tmp1
			first, second = tmp1, tmp2
