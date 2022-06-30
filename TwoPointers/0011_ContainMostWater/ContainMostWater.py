# This solution uses two pointers to find the max area. Starting at the ends, we calculate the area with the min
# height of the two points and the distance between them. The lesser height gets incremented towards the other pointer
# at each iteration.
class Solution:
	def maxArea(self, height: List[int]) -> int:
		res = 0
	    l, r = 0, len(height) - 1

		while l < r:
			area = (r - l) * min(height[l], height[r])
			res = max(res, area)

			if height[l] < height[r]:
				l += 1
			else:
				r -= 1

		return res
