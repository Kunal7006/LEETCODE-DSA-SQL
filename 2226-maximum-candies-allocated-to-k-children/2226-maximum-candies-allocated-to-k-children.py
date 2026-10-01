class Solution:
    def canGiveCandies(self,candies,mid,k):
        childCount =0

        for i in range(len(candies)):
            childCount+= candies[i]//mid

            if childCount>=k:
                return True
        return False
    def maximumCandies(self, candies: list[int], k: int) -> int:
        low = 1
        high = max(candies)

        while low <= high:
            mid = low +(high-low)//2

            if self.canGiveCandies(candies,mid,k):
                low = mid +1
            else:
                high = mid -1
        return high