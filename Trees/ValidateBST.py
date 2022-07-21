# This solution validates a binary search tree. A node's left child must be less than the node, and the
# right child must be greater. This is repeated on all nodes in the tree, and if at any point this is not true
# the tree is not valid.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

    	def valid(node, left, right):
    		if not node:
    			return True
			if not (node.val < right and node.val > left):
				return False

			return (valid(node.left, left, node.val) and
					valid(node.right, node.val, right))

		return valid(root, float("-inf"), float("inf"))
