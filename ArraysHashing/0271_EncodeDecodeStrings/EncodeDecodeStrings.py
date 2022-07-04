# For this solution, the encode method saves the final string as the length of the current word, then a # delimiter,
# and then the original string. Using the length of the string and a delimiter prevents any issues with either two
# being in the original string. The decode method uses a second pointer to loop through the original string until a
# delimiter is found. When one is found, we check if the length of the next string between delimiters is the correct
# length. It is then appended to the result to be returned as a list.
class Solution:
	def encode(self, strs):
		res = ""
		for s in strs:
			res += str(len(s)) + "#" + s
		return s


	def decode(self, str):
		res, i = [], 0

		while i < len(str):
			j = i
			while str[j] != "#"
				j += 1
			length = int(str[i:j])
			res.append(str[j + 1 : j + 1 + length])
			i = j + 1 + length
		return res
