# This solution iterates through every bit in the int, which is of length 32, to reverse it.
# The current bit is found by shifting the number n to the right by i places. It is then appended to the result with
# an OR statement, which is left shifted by 31 - i places, which would put the bits in reverse order. For example,
# in the first iteration, the last bit will be grabbed, and then left shifted 31 places to put the bit to the beginning.
class Solution:
	def reverseBits(self, n: int) -> int:
		res = 0

		for i in range(32):
			bit = (n >> i) & 1
			res = res | (bit << (31 - i))
		return res
