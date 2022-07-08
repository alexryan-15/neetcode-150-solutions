# This solution uses the current digit and a running result value to find the solution. At every iteration, the
# result is increased by a factor of 10 and the current digit is added. If at any point the result goes outside
# the bounds for an integer, 0 is returned immediately, since the result will only go farther outside those bounds.
class Solution:
    def reverse(self, x: int) -> int:

        MIN = -1 * 2**31
        MAX = 2**31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > MAX // 10 or
                (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or
                (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit

        return res
