# This solution reverses each group of K nodes by first getting the kth node to define
# the groups to be reversed. If one does not exist, then we are at the last group of the
# list and this group has less than k nodes, which means we are done. If not, we just
# reverse the current group and then move on to the next group. Two pointers are kept
# for the group's previous node and the group's next node to assist in moving between groups
# and in reversing of the group.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		dummy = ListNode(0, head)
		groupPrev = dummy

		while True:
			kth = self.getKth(groupPrev, k)
			if not kth:
				break
			groupNext = kth.next

			prev, curr = kth.next, groupPrev.next

			while curr != groupNext:
				tmp = curr.next
				curr.next = prev
				prev = curr
				curr = tmp

			tmp = groupPrev.next
			groupPrev.next = kth
			groupPrev = tmp

		return dummy.next
			

	def getKth(self, curr, k):
		while curr and k > 0:
			curr = curr.next
			k -= 1
		return curr
