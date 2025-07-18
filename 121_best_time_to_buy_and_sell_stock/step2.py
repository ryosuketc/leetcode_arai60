class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        min_prices_from_left = [prices[0]] * len(prices)
        for i in range(1, len(prices)):
            min_prices_from_left[i] = min(min_prices_from_left[i - 1], prices[i])
        max_prices_from_right = [prices[-1]] * len(prices)
        for i in reversed(range(len(prices) - 1)):
            max_prices_from_right[i] = max(max_prices_from_right[i + 1], prices[i])
        
        max_profit = 0
        for min_price, max_price in zip(min_prices_from_left, max_prices_from_right):
            max_profit = max(max_profit, max_price - min_price)
        
        return max_profit
