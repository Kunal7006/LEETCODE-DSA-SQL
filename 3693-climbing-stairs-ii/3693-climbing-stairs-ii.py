class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp =[0]*(n+1)

        for i in range(n-1,-1,-1):
            cost = float('inf')

            j = i+1
            if j<=n:
                cost = min(cost,dp[j]+costs[j-1] +(j-i)*(j-i))
            j = i+2
            if j<=n:
                cost = min(cost,dp[j]+costs[j-1] +(j-i)*(j-i))
            j = i+3
            if j<=n:
                cost = min(cost,dp[j]+costs[j-1] +(j-i)*(j-i))
            dp[i]=cost
        return dp[0]