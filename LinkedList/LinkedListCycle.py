# This solution determines if there is a cycle in the linked list by using a fast pointer and
# a slow pointer. The fast pointer moves twice as fast as the slow pointer, which means that
# it will cycle back and catch up to the slow pointer if there is a cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
