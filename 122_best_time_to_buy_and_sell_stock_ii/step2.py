class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        def find_next_bottom(start_index):
            i = start_index
            while i + 1 < len(prices) and prices[i] >= prices[i + 1]:
                i += 1
            return i

        def find_next_peak(start_index):
            i = start_index
            while i + 1 < len(prices) and prices[i] <= prices[i + 1]:
                i += 1
            return i
        
        profit = 0
        i = 0
        while i < len(prices) - 1:
            bottom = find_next_bottom(i)
            peak = find_next_peak(bottom)
            profit += prices[peak] - prices[bottom]
            i = peak
        return profit


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        # Max profit on the first day
        profit_hold_stock_previous_day = -prices[0]
        profit_not_hold_stock_previous_day = 0
        for i in range(1, len(prices)):
            # Buy stock
            profit_hold_stock = max(profit_hold_stock_previous_day, profit_not_hold_stock_previous_day - prices[i])
            # Sell stock
            profit_not_hold_stock = max(profit_not_hold_stock_previous_day, profit_hold_stock_previous_day + prices[i])
            profit_hold_stock_previous_day = profit_hold_stock
            profit_not_hold_stock_previous_day = profit_not_hold_stock
        return max(profit_hold_stock_previous_day, profit_not_hold_stock_previous_day)


class Solution3_2:
    def maxProfit(self, prices: List[int]) -> int:
        # Max profit on the first day
        profit_hold_stock = -prices[0]
        profit_not_hold_stock = 0
        for i in range(1, len(prices)):
            # Back up the current data (serves as the figure on the previous day)
            profit_hold_stock_tmp = profit_hold_stock
            # Buy stock
            profit_hold_stock = max(profit_hold_stock, profit_not_hold_stock - prices[i])
            # Sell stock
            profit_not_hold_stock = max(profit_not_hold_stock, profit_hold_stock_tmp + prices[i])
        return max(profit_hold_stock, profit_not_hold_stock)
