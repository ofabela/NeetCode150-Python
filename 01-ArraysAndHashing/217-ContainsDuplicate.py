class Solution:
	def contains_duplicate(self, nums: list[int]) -> bool:
		visited = {}

		for num in nums:
			if num not in visited:
				visited[num] = 1
			else:
				return True
		return False

ex = Solution()
#Output: True 
print(f'{ex.contains_duplicate([1, 2, 3, 1])= }')
#Output: False 
print(f'{ex.contains_duplicate([1, 2, 3, 4])= }')