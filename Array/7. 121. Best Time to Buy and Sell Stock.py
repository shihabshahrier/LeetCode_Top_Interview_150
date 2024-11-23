# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        max_profit = 0
        for i in prices:
            if i < b:
                b = i
            x = i - b
            if x > max_profit:
                max_profit = x
        return max_profit

# Easy | Self explained 
