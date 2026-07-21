class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curr = prices[0]
        profit = 0
        for i in range(1,n):
            curr = min(curr,prices[i])
            profit = max(profit,prices[i] - curr)
        return profit


             


        