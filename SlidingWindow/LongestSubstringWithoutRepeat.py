# A set is used to track duplicate letters in the input. When a duplicate is found, it is removed from the set and
# the left pointer is incremented. When finding a new character that is not in the set, it is added to the set.
# the length of the solution is the max distance between the left and right pointers that contains no duplicates.
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		charSet = set()
		l = 0
		res = 0

		for r, i in enumerate(s):
			while i in charSet:
				charSet.remove(s[l])
				l += 1
			charSet.add(i)
			res = max(res, r - l + 1)
		return res
