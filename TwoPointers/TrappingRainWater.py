# This solution uses two pointers and tracks the max height before and after the current height.
# At every iteration, one of the maxes is updated to be the max of itself and the current height.
# The difference between this new max and the current height is then added to the result, which is either
# zero or some actual value of water.
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
        	return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
