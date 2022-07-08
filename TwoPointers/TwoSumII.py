# This solution uses two pointers to find the target number. Since the array is in non-decreasing order,
# If the current sum is two large, we move the right pointer to the left, which would be <= the current number,
# and vice versa. We then return the indicies of the two numbers plus 1, since it is a 1-indexed array.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
