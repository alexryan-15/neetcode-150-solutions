# This solution first removes all non-alphanumeric characters from the string to only compare the letters.
# Then, it uses two pointers, from the beginning and end of the string, to compare equality
# and determine if the string is a palindrome. 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True