# This solution uses sets to find the total length of nums. Since a set only keeps unique values, if the
# length of the set is the same length as the original input, then the array does not contain any duplicates
class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		s = set(nums)
		if len(s) == len(nums):
			return False
		return True

# This solution uses a dictionary to keep track of numbers that were already encountered. If a number reappears,
# then it will be in the dictionary and we can return True. If there are no duplicates, then we will pass through the
# entire input and return False
class Solution2:
	def ContainsDuplicate(self, nums: List[int]) -> bool:
		duplicates = {}
		for i in nums:
			if i in duplicates:
				return True
			duplicates[i] = 1
		return False
