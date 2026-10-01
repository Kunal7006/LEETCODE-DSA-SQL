class Solution:
    def canShip(self,weights,mid):
        load =0
        days =1
        for x in weights:
            if load + x>mid:
                days +=1
                load = x
            else:
                load +=x
        return days
        
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <=high:
            mid = low + (high-low)//2

            if self.canShip(weights,mid)<=days:
                high = mid -1
            else:
                low = mid +1
        return low