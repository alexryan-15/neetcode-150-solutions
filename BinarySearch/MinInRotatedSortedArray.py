# Start with two pointers, one on each side of the list. We want to continually find the min with each cut of
# the list. If our number on the left is less than the number on the right, then the min is either the left pointer
# or the previous min that was found, since every number between the left and right pointer would be greater than
# the left. If the mid point is greater than the left point, we search the right half of the list, if not,
# then we search the left half of the list.
class Solution:
	def findMin(self, nums: List[int]) -> int:
		res = nums[0]
		l, r = 0, len(nums) - 1

		while l <= r:
			if nums[l] < nums[r]:
				res = min(res, nums[l])
				break

			m = (l + r) // 2
			res = min(res, nums[m])
			if nums[m] >= nums[l]:
				l = m + 1
			else:
				r = m - 1
		return res
