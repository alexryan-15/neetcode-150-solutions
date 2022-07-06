# Start with two pointers at the beginning and end of the list. Create a middle point of those two pointers.
# If the target number is the middle number, return it, if not we have to check for which half to search.
# If the left pointer is less than the middle pointer, then we check if the target outside the range from the
# left pointer to the middle. If it is, the new left pointer is m + 1. If the target is in that range, then
# the new right pointer is m - 1. If the middle pointer is less than the left pointer, we do the range checking
# on the right half of the list. This cuts the list in half every pass until we find our answer.
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums) - 1

		while l <= r:
			m = (l + r) // 2
			if target == nums[m]:
				return m

			if nums[l] <= nums[m]:
				if target > nums[m] or target < nums[l]:
					l = m + 1
				else:
					r = m - 1
			else:
				if target < nums[m] or target > nums[r]:
					r = m - 1
				else:
					l = m + 1
			return -1
