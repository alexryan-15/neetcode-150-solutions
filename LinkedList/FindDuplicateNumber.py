# This problem relies on finding a cycle using Floyd's cycle detection. Slow and
# fast pointers are used to find the cycle and hence the duplicate number.
# There are two phases of this algorithm with the pointers. The second iteration
# is where the answer is found.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    	slow, fast = 0, 0
    	while True:
    		slow = nums[slow]
    		fast = nums[nums[fast]]
    		if slow == fast:
    			break

		slow2 = 0
		while True:
			slow = nums[slow]
			slow2 = nums[slow2]
			if slow == slow2:
				return slow
