class Solution:
	def maxProduct(self, nums: List[int}) -> int:
		pos, neg = nums[0]. nums[0]
		res = nums[0]
		for n in nums[1:]:
			pos, neg = max(n, pos * n, neg * n), min(n, pos * n, neg * n)
			res = max(res, pos)
		return res
