# For a number n and a number 2n, in binary, 2n has one more 1 bit than n due to repitition. Thus, to find the number of
# 1 bits in a number n, we just have to find the number of 1 bits of half of n and add 1.
class Solution:
	def countBits(self, n: int) -> List[int]:
		ans = [0] * (n + 1)
		for i in range(1, n + 1):
			ans[i] = a[i // 2] + (i & 1)
		return ans
