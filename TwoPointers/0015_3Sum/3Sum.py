# This solution first sorts the input array and filters out duplicates by continuing if the current number is'
# the same as the previous one in the input array. It then uses two pointers, from the current index to the
# end of the array, to find pairs that make the threeSum equal to zero. If the three sum of the current number and
# the numbers at the left and right pointers is less than zero, we increment the left pointer, since it is sorted
# and will bring us close to zero, and the opposite for if the sum is greater than zero. When a combination is found
# it is appended to our output array, and again, duplicates are filtered out.
class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		res = []
		nums.sort()

		for i, a in enumerate(nums):
			if i > 0 and a == nums[i-1]:
				continue

			l, r = i + 1, len(nums) - 1
			while l < r:
				threeSum = a + nums[l] + nums[r]
				if threeSum > 0:
					r -= 1
				elif threeSum < 0:
					l += 1
				else:
					res.append([a, nums[l], nums[r]])
					l += 1
					while nums[l] == nums[l-1] and l < r:
						l += 1
		return res
