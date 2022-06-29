# Uses the built in sorted function to sort the letters of the word and check if they are equal
class Solution:
	def isAnagram(self, s: str, t:str) -> bool:
		return sorted(s) == sorted(t)

# Uses collections.Counter to count the occurrences of each letter in the words
from collections import Counter
class Solution2:
	def isAnagram(self, s:str, t:str) -> bool:
		return Counter(s) == Counter(t)

# Initially checks the lengths of s and t, if they are different, they can not be anagrams.
# Uses the count function to check occurences of each letter.
class Solution3:
	def isAnagram(self, s:str, t:str) -> bool:
		if len(s) != len(t):
			return False

		for c in set(s):
		if s.count(c) != t.count(c):
			return False

		return True
