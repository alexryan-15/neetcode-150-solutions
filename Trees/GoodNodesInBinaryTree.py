# This solution finds and returns the number of good nodes in a binary tree. A good node X is good if in the path
# from the root to X, there are no nodes with a value greater than X. This uses DFS and tracks the maximum
# value in the path so far. If the current node is greater than this max value, then it is a good node. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

		def dfs(node, maxVal:
			if not node: return 0

			res = 1 if node.val >= maxVal else 0
			maxVal = max(maxVal, node.val)
			res += dfs(node.left, maxVal)
			res += dfs(node.right, maxVal)
			return res

		return dfs(root, root.val)
