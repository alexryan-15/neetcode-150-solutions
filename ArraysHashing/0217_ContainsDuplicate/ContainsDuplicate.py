# Using sets, much simpler solution, might not work in other languages
class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		s = set(nums)
		if len(s) == len(nums):
			return False
		return True

# Other solution using a dictionary, recreatable in most languages
class Solution:
	def ContainsDuplicate(self, nums: List[int]) -> bool:
		duplicates = {}
		for i in nums:
			if i in duplicates:
				return True
			duplicates[i] = 1
		return False
