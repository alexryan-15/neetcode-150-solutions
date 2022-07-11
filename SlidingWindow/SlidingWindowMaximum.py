# This solution uses a double ended decreasing queue to track the maximum sliding window.
# We keep popping smaller values in the queue while they exist and then append the
# larger values that would make a greater maximum window. The queue always holds the
# last sliding window of k elements.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
