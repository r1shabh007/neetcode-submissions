class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - buy_price
            if profit > max_profit:
                max_profit = profit
            if prices[i] < buy_price:
                buy_price = prices[i]
        return max_profit
