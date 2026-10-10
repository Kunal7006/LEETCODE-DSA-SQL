class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)

        countDiff =[0]*100001

        for i in range(n):
            d = abs(nums1[i]-nums2[i])
            countDiff[d]+=1
        
        k = k1 + k2

        for currDiff in range(100000,0,-1):
            if k<=0:
                break
            countOps = min(countDiff[currDiff],k)

            countDiff[currDiff]-= countOps
            countDiff[currDiff-1]+=countOps
            k-=countOps
        
        result = 0

        for d in range(1,100001):
            result += (countDiff[d] * d*d)
        return result;