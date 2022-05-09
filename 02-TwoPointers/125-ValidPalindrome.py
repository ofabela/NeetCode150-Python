class Solution:
	"""
	Easy
	Given a string , return true if it is a palindrome, or false otherwise.

	Example
	Input: s = "A man, a plan, a canal: Panama"
	Output: true
	"""

	def valid_palindrome_smells(self, s: str) -> bool:
		s = ''.join([i.lower() for i in s if i.isalnum()])
		left, right = 0, len(s)-1

		print(s)
		for _ in range(0, len(s)//2):
			if s[left] != s[right]:
				return False
			left += 1
			right -= 1
		return True

	def valid_palindrome_better(self, s: str) -> bool:
		in_order = [i.lower() for i in s if i.isalnum()]
		reverse_order = [i.lower() for i in s[::-1] if i.isalnum()]

		return in_order == reverse_order

	def valid_palindrome_best(self, s: str) -> bool:
		l, r = 0, len(s)-1
		while l < r:
			if not s[l].isalnum() and l < r:
				l += 1
				continue
			if not s[r].isalnum() and r > l:
				r -= 1
				continue

			if s[l].lower() != s[r].lower():
				return False
			l, r = l + 1, r - 1
		return True


result = Solution()
expected = result.valid_palindrome_smells("A man, a plan, a canal: Panama")
actual = True

print(expected, actual)

expected = result.valid_palindrome_better("A man, a plan, a canal: Panama")
print(expected, actual)

expected = result.valid_palindrome_best("A man, a plan, a canal: Panama")
print(expected, actual)
