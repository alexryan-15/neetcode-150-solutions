# This solution first copies all of the old nodes using a hashmap to map the old nodes to the
# new ones. This is used to create the deep copy, which is what the problem requires.
# Then, the next and random pointers are updated in the new copy with the use of the hashmap.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
	 def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		oldToCopy = { None : None }

		cur = head
		while cur:
			copy = Node(cur.val)
			oldToCopy[cur] = copy
			cur = cur.next

		cur = head
		while cur:
			copy = oldToCopy[cur]
			copy.next = oldToCopy[cur.next]
			copy.random = oldToCopy[cur.random]
			cur = cur.next

		return oldToCopy[head]
