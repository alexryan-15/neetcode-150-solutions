# For this problem, we want to keep track of the max sum that we have found so far, and see if adding the current
# number increases that. This solution iterates through the input array, and keeps track of the max sum found so far.
# If it ever goes negative, it is reset to zero. We keep track of the max so far by taking the max of the max that we
# have found previously and the current max.
class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		maxSub = nums[0]
		curSum = 0

		for n in nums:
			if curSum < 0:
				curSum = 0
			curSum += n
			maxSub = max(maxSub, curSum)
		return maxSub
