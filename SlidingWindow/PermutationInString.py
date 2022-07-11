# This solution uses a arrays for each input to count the number of instances of each
# character. We count the instances of each character first by looping through the first
# input and adding to the array with ord. Then in the sliding window, we decrement in the
# array for the second input on every iteration. We return whether the arrays are equal.
class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		m1, m2 = [0]*26, [0]*26

		if (len(s1) > len(s2)):
			return False

		for i in range(len(s1)):
			m1[ord(s1[i]) - ord('a')] += 1
			m2[ord(s2[i]) - ord('a')] += 1

		for i in range(len(s2) - len(s1)):
			if m1 == m2:
				return True

			s2[ord(s2[i]) - ord['a']] -= 1
			s2[ord(s2[i + len(s1)]) - ord['a']] -= 1

		return m1 == m2
