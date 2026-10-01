class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        low =0
        high = n-1

        while low <= high:
            mid = low + (high - low)//2

            if citations[mid]== n - mid:
                return n-mid
            elif citations[mid]>n-mid:
                high = mid -1
            else:
                low = mid +1
        return n - low