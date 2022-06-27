# Two solutions, the first has python specific functions which may or may not be available in other languages
class Solution:
	def hammingWeight(self, n: int) -> int:
		return bin(n).count('1')

# Other, more general, solution
class Solution:
	def hammingWeight(self, n: int) -> int:
		c = 0
		while n:
			c += n % 2
			n = n >> 1
		return c
