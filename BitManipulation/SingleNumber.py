# In order to find the missing number in the input array, we can just XOR all of the numbers together
# and this will give us the solution.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
