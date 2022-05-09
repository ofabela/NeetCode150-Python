class Solution:
	def search(self, nums: list[int], target: int) -> int:
		low, high = 0, len(nums) - 1

		while low <= high:
			# middle is also (high + low) // 2 but
			# bounded primtive types might overflow 
			middle = low + (high - low) // 2
			if nums[middle] < target:
				low = middle + 1
			elif nums[middle] == target:
				return middle
			else:
				high = middle - 1
		return -1

s = Solution()
print(s.search([-1,0,3,5,9,10,12], 9))
