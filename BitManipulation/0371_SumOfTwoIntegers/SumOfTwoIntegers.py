# This solution has to use a bit mask when iterating through the second number, b. The sum variable is determined by
# taking the XOR of the two numbers at the end position, and the carry is determined by taking an AND shifted to the
# left by one. The new a value is then the current sum and the new b value is the carry. As long as the carry exists,
# we continue doing this. At the end, we return a.
class Solution:
	def getSum(self, a: int, b: int) -> int:
		mask = 0xFFFFFFFF
		while b:
			sum = (a ^ b) & mask
			carry = ((a & b) << 1) & mask
			a = sum
			b = carry

		if (a >> 31) & 1:
			return ~(a ^ mask)
		return a
