# This solution uses a stack that adds pairs of temperatures and their indicies to determine the number of days until
# a greater temperature is found. If the current temperature is greater than the one on the top of the stack, we can
# pop from the stack and add the popped value to the result. If this isn't true, then we can append more items on to
# the stack until there is a number that is greater than one on top.
class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		res = [0] * len(temperatures)
		stack = []

		for i, t in enumerate(temperatures):
			while stack and t > stack[-1][0]:
				sT, sI = stack.pop()
				res[sI] = (i - sI)
			stack.append([t, i])
		return res
