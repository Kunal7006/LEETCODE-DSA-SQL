class Solution:
    def count(self,mid,m,n):
        count = 0
        for i in range(1,m+1):
            temp = min(mid//i,n)
            count += temp
        return count
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low = 1
        high = m * n

        while low<=high:
            mid = low + (high - low)//2

            capacity = self.count(mid,m,n)

            if capacity>=k:
                high = mid -1
            else:
                low = mid +1
        return low