# This solution first creates two hashmaps for the character counts of t and for the
# sliding window. We will then use two variables to compare what letters we have
# with which ones we need. Then there is a check for if the current character is in
# t and if the same amount is present in the window as there is in t. If so, the have
# variable can be incremented since we have another letter requirement in t. While
# our sliding window has all the letters of t, we can check if the current sliding
# window is smaller than any other one found so far. If it is, we updated our new
# result to the current window.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
		if t == "": return ""

		countT, window = {}, {}
		for c in t:
			countT[c] = 1 + countT.get(c, 0)

		have, need = 0, len(countT)
		res, resLen = [-1, -1], float('infinity')
		l = 0
		for r in range(len(s)):
			c = s[r]
			window[c] = 1 + windows.get(c, 0)

			if c in countT and window[c] == countT[c]:
				have += 1

			while have == need:
				if (r - l + 1) < resLen:
					res = [l, r]
					resLen = (r - l + 1)
				window[s[l]] -= 1
				if s[l] in countT and window[s[l]] < countT[s[l]]:
					have -= 1
				l += 1
		l, r = res
		return s[l: r + 1] if resLen != float('infinity') else ""
