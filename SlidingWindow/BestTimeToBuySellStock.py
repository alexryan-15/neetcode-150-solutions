# This solution uses the sliding window technique with two pointers to keep track of the largest profit.
# We find the profit at every iteration until the right pointer has reach the end of the input array and
# compare it to the max profit found so far. The right pointer moves one spot to the right at each iteration
# and the left pointer only moves to the right when the price at the left pointer is greater than the price at
# the right, i.e. there is a negative profit.
class Solution:
	def MaxProfit(self, prices: List[int]) -> int:
	l, r = 0, 1
	maxProfit = 0

	while r < len(prices):
		if prices[l] < prices[r]:
			profit = prices[r] - prices[l]
			maxProfit = max(maxProfit, profit)
		else:
			l = r
		r += 1
	return maxProfit
