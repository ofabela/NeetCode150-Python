class Solution:
	def is_anagram(self, s: str, t: str) -> bool:
		anagram_set = set(s + t)
		for ch in anagram_set:
			if s.count(ch) != t.count(ch):
				return False
		return True

Ex1 = Solution()
print(f'Should be True\n{Ex1.is_anagram("anagram", "nagaram")=}')

print(f'Should be False\n{Ex1.is_anagram("rat", "car")=}')