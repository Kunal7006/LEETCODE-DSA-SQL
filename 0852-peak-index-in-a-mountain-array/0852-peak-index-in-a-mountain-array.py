class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)
        l =0
        r = n-1

        while l<=r:
            mid = l +(r-l)//2

            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]< arr[mid+1]:
                l = mid +1
            else:
                r = mid -1
            