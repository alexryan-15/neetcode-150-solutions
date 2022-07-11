# For this solution, we have to consider the previous product subarray and the current product.
# If the previous product is positive, and multiplying by the current number is also positive, it becomes our new
# answer. We iterate through the input array with this idea and keep track of the max product that we have found
# so far. The pos variable is used to keep track of the current largest positive product and the neg variable
# to keep track of the largest negative product, if abs(pos) < abs(neg) and the next value is negative as well,
# using neg would actually give us the larger product.
class Solution:
	def maxProduct(self, nums: List[int}) -> int:
		pos, neg = nums[0] nums[0]
		res = nums[0]
		for n in nums[1:]:
			pos, neg = max(n, pos * n, neg * n), min(n, pos * n, neg * n)
			res = max(res, pos)
		return res
