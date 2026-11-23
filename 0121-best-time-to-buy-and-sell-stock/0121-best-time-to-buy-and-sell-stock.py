class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        minPrice = float('inf')
        maxPro=0

        for i in range(n):
            minPrice = min(minPrice,prices[i])
            maxPro = max(maxPro,prices[i]-minPrice)
        return maxPro