# This solution does a level order traversal of a binary tree. A deque is used and starts with the root.
# The nodes are added from left to right and then it moves to the next level to get the correct order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    	res = []
    	q = collections.deque()
    	if root: q.append(root)

    	while q;
    		val = []

    		for i in range(len(q))"
    			node = q.popleft()
    			val.append(node.val)
    			if node.left: q.append(node.left)
    			if node.right: q.append(node.right)
			res.append(val)
		return res
