# First solution, creates a dictionary to hold final answer of anagram groups. For every string in the input, creates
# an array of size 26 to correspond to letters of the alphabet. Then, loops through each character of the string
# and increments the array's index which corresponds to the current letter. Uses the ord function to do this. For example,
# the letter 'a' corresponds to index 0, letter 'b' to index 1, and so on. So if we want to count a letter 'c', then we
# need to increment index 2 in the array, which can be done by taking the ASCII value of the 'c', and subtracting the
# ASCII value of 'a'. After finished with a word, we append it to the dictionary with the array of counts as the key
# and the string as the value. If words are anagrams, then the count array will have multiple values.
class Solution:
	def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
		d = collections.defaultdict(list)

		for s in strs:
			count = [0] * 26
			for c in s:
				count[ord(c) - ord('a')] += 1
			d[tuple(count)].append(s)

		return d.values()

# Second solution, also using a dictionary. Adds sorted words to the dictionary as the key.
# If the key already exists, append the original word as a value. If not, create a new key:value pair.
class Solution2:
	def groupAnagrams(self, strs: List[str]) ->List[List[str]]:
		d = {}

		for i in range(len(strs)):
			s = ''.join(sorted(strs[i]))
			if s not in d:
				d[s] = [strs[i]]
			else:
				d[s].append(strs[i])

		return d.values()
