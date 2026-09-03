class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        minimum = nums1[0]
        allEven = True

        for x in range(n):
            minimum = min(minimum,nums1[x])

            if nums1[x] % 2 != 0:
                allEven = False

        if minimum % 2 !=0:
            return True
        if allEven:
            return True
        
        return False