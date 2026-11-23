class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        t=[[0]*2 for _ in range(n+1)]

        t[n][0]=0
        t[n][1]=0

        for i in range(n-1,-1,-1):
            for buy in range(2):
                profit =0
                if buy:
                    profit = max(-prices[i] +t[i+1][0],t[i+1][1])
                else:
                    profit = max(prices[i]+t[i+1][1],t[i+1][0])
                t[i][buy]=profit
        
        return t[0][1]