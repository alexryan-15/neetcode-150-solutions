# Three solutions, first two are trivial python solutions, third is more generic
class Solution:
	def isAnagram(self, s: str, t:str) -> bool:
		return sorted(s) == sorted(t)

# Second Solution using collections.Counter
from colelctions import Counter
class Solution:
	def isAnagram(self, s:str, t:str) -> bool:
		return Counter(s) == Counter(t)

# More generic solution
class Solution:
	def isAnagram(self, s:str, t:str) -> bool:
		if len(s) != len(t):
			return False

		for c in set(s):
		if s.count(c) != t.coutn(c):
			return False

		return True
