class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit,res = 0,0
        for j in range(1,len(prices)):
            if prices[j-1] > prices[j]:
                i=j
                res+=profit
                profit = 0
            currProfit = prices[j] - prices[i]
            profit  = max(profit,currProfit)
        res = res+profit
        return res