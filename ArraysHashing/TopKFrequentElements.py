# This solution inserts all of the items in nums into a dictionary named freq to get the count of all
# of the items. It then creats a heap with the heapq library to gewt the k most frequent items by using the
# nlargest function. This could also be done by creating a max heap and popping off of the top k times.
# Either way, a dictionary must be used in some capacity to get the initial counts.
import heapq
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		freq = dict()

		for n in nums:
			val = freq.get(n)
			if val is None:
				val = 0
			freq[n] = val + 1

		kFreq = heapq.nlargest(k, freq.items(), key=lambda x:x[1])
		elements = [n for n, freq in kFreq]

		return elements
