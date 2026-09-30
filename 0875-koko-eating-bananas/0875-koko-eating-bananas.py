class Solution:
    def canEatAll(self,piles,mid,h):
        actualHours = 0
        for x in piles:
            actualHours+= x//mid

            if x%mid !=0:
                actualHours+=1
        return actualHours<=h

    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        l =1
        r = max(piles)

        while l<r:
            mid = l + (r-l)//2

            if self.canEatAll(piles,mid,h):
                r = mid
            else:
                l = mid +1
        return l