# First solution, using ASCII values and a dictionary
class Solution:
	def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
		d = collections.defaultdict(list)

		for s in strs:
			count = [0] * 26
			for c in s:
				count[ord(c) - ord('a')] += 1
			d[tuple(count)].append(s)

		return d.values()

# Second solution, more generic with a dictionary
class Solution:
	def groupAnagrams(self, strs: List[str]) ->List[List[str]]:
		d = {}

		for i in range(len(strs)):
			s = ''.join(sorted(strs[i]))
			if s not in d:
				d[s] = [strs[i]]
			else:
				d[s].append(strs[i])

		return d.values()
