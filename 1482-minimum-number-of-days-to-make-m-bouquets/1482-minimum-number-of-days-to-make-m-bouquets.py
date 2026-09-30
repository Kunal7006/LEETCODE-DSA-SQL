class Solution:
    def canMakeMBoquet(self,bloomDay,mid,k):
        boqCount =0
        consecutiveDays =0

        for x in bloomDay:
            if x<=mid:
                consecutiveDays +=1
            else:
                consecutiveDays =0

            if consecutiveDays ==k:
                boqCount+=1
                consecutiveDays =0
        return boqCount
        
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        start =0
        end = max(bloomDay)
        minDays = -1

        while start <= end:
            mid = start + (end-start)//2

            if self.canMakeMBoquet(bloomDay,mid,k)>=m:
                minDays = mid
                end = mid -1
            else:
                start = mid +1
        return minDays