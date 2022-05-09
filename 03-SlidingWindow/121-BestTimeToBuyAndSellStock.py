class Solution:
	"""
	You are given an array prices where prices[i] is the price of a given stock
	on the ith day. You want to maximize your profit by choosing a single day to 
	buy one stock and choosing a different day in the future to sell that stock.

	Return the maximum profit you can achieve from this transaction. If you
	cannot achieve any profit, return 0.
	"""
	def max_profit(self, prices: list[int]) -> int:
		l, r = 0, 1
		max_transaction = 0

		while r < len(prices):
			if prices[l] < prices[r]:
				profit = prices[r] - prices[l]
				max_transaction = max(max_transaction, profit)
			else:
				l = r
			r += 1
		return max_transaction 


test = Solution()

prices = [7,1,5,3,6,4]

print(f'{test.max_profit(prices)=}')
#actual =
expected = 5
