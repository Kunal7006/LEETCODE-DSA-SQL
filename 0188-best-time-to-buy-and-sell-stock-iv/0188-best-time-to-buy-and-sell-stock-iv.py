class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        t=[[[0]*(k+1) for _ in range(2)]for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for b in range(2):
                for cap in range(1,k+1):
                    profit =0
                    if b:
                        profit = max(-prices[i]+t[i+1][0][cap],t[i+1][1][cap])
                    else:
                        profit = max(prices[i]+t[i+1][1][cap-1],t[i+1][0][cap])
                    t[i][b][cap]=profit
        return t[0][1][k]