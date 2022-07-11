# This solution uses a binary search to calculate the rate k which is needed to eat
# all of the bananas. The rate is going to be somewhere between the min and max
# values of piles. We do binary search to find the minimum value where all of the
# bananas can be eaten in H hours.
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ((p-1)//m) + 1
            if totalTime <= H:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
