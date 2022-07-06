# This solution uses a set to track the longest consecutive sequence in the input array. For every number in the
# array, if the previous number is not in the set, the current length of the sequence is reset to 1. If
# the previous number is in the input, then the length is increased. We take the max of the length of the current
# sequence and the length of the longest sequence that we have found so far.
class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		numSet = set(nums)
		longest = 0

		for n in nums:
			if (n - 1) not in numSet:
				length = 1
				while (n + length) in numSet:
					length += 1
				longest = max(length, longest)
		return longest
