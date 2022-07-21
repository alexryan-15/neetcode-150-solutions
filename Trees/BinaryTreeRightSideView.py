# This solution uses a deque to find the right side view of a binary tree. This means taking the right most
# node on every level of the binary tree. We want to add all items of a level to the queue and then the item
# that was added last will be the right most node of the level. We can then add this to our results and continue
# by adding the children of the nodes on the current level.

# Definition for a binary tree node. 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
    	res = []
    	q = collections.deque([root])

    	while q:
    		rightSide = None

    		for i in range(len(q)):
    			node = q.popleft()
    			if node:
    				rightSide = node
    				q.append(node.left)
    				q.append(node.right)
				if rightSide:
					res.append(rightSide.val)
			return res
