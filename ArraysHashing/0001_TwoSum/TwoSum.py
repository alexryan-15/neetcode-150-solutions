# This solution uses a dictionary to keep track of the numbers that were previously iterated through in nums
# If the difference betweeen the target number and the current number has been added to the dictionary, then the solution
# Is the current number and the previous one that was added. This allows for the algorithm to run in O(n).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
