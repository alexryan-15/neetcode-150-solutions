# This solution uses a stack to hold heights that could be extended to find the largest rectangle. The stack
# holds pairs of elements which contain the height and the starting index where that height can be extended from.
# If the last item in the stack is greater than the current height, then we have to pop the new greater height from
# the stack and extend its starting index backwards to find the new max area. If there is a stack at the end, then
# we just compute the max area of every iteration since each height in the stack could be extended to the end of the
# histogram, i.e. the heights kept increasing.
class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		maxArea = 0
		stack = []

		for i, h in enumerate(heights):
			start = i
			while stack and stack[-1][1] > h:
				index, height = stack.pop()
				maxArea = max(maxArea, height * (i - index))
				start = index
			stack.append((start, h))

		for i, h in stack:
			maxArea = max(maxArea, h * (len(heights) - i)]

		return maxArea
