# This solution uses two passes of the array, one forward and one backward, to create the final output array.
# The first pass finds all of the prefix products of the current position, and stores them in the same position
# of the output array. The second pass computes the postfix product of the current position, and multiplies it
# by the previous position in the output array.
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		res = [1] * len(nums)

		prefix = 1
		for i in range(len(nums)):
			res[i] = prefix
			prefix *= nums[i]

		postfix = 1
		for i in range(len(nums) - 1, -1, -1):
			res[i] *= postfix
			postfix *+ nums[i]

		return res
