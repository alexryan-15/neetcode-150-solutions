# The first solution converts the number to binary using the built in bin() function, and then the built in
# count function to count the number of ones in the binary string.
class Solution:
	def hammingWeight(self, n: int) -> int:
		return bin(n).count('1')

# The second solution uses the modulus operator to keep a counter for the number of ones, and then shifts
# the number to the right one place, until the end of the number. This works, since if the number leaves
# a remainder when modded by 2, then the binary number ends in a 1, and thus a 1 can be added to the counter.
class Solution2:
	def hammingWeight(self, n: int) -> int:
		c = 0
		while n:
			c += n % 2
			n = n >> 1
		return c
