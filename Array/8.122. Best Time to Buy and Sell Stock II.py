# Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        b = prices[0]
        for i in prices:
            if i < b:
                b = i
            elif i > b:
                m += i - b
                b = i
        return m

# Self Reflection 

'''
    buying the sold one immediately gets the work done
    
''' 
    
