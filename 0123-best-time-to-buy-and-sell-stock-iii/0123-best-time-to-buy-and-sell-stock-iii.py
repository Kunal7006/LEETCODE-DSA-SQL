class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        t=[[[0]*3 for _ in range(2)]for _ in range(n+1)]

        # base cases  no need to initialize as dp table is already initialized with 0
        # if cap ==0 i and b can be anything
        # for i in range(n):
        #     for b in range(2):
        #         t[i][b][0]=0
        
        # if i == n then cap and b can be anything

        # for b in range(1):
        #     for cap in range(2):
        #         t[n][b][cap]=0

        for i in range(n-1,-1,-1):
            for b in range(2):
                for cap in range(1,3):
                    profit =0
                    if b:
                        profit= max(-prices[i]+t[i+1][0][cap],t[i+1][1][cap])
                    else:
                        profit =max(prices[i]+t[i+1][1][cap-1],t[i+1][0][cap])
                    t[i][b][cap]=profit
        return t[0][1][2]