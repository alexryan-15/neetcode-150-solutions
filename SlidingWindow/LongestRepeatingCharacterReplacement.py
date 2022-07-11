# This solution uses a sliding window and expands if we can change the character in the current position,
# and contracts when the window becomes greater than k. This uses a hashmap to track the counts of the
# characters in the input array, which are used to move the sliding window.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r, i in enumerate(s):
            count[i] = 1 + count.get(i, 0)
            maxf = max(maxf, count[i])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
