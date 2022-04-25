class Solution():
	"""
	Easy
	"""
	def two_sum(arr, target):

		dic = {}
		for index, value in enumerate(arr):
			b = target - value 
			if b not in dic:
				dic[value] = index
			else:
				return [index, dic[b]]

arr = [2, 1, 5, 3]
target = 4

print(two_sum(arr, target))