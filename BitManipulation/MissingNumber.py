# This solution starts with res equal to the length of the input array, and then for the range of that array,
# the result is increased by the difference of the index and the number at that index. This means that every index
# from 1 to k will be added to the result, but not every number from 1 to k will be subtracted. This means that the
# only number that won't be subtracted will be the missing number.
class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		res = len(nums)

		for i in range(len(nums)):
			res += (i - nums[i])
		return res
