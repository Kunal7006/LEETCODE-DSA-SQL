from bisect import bisect_right

class Solution:

    def countOfSmallerOrEqualElements(self, matrix, mid):
        n = len(matrix)
        m = len(matrix[0])
        count = 0

        for i in range(n):
            count += bisect_right(matrix[i], mid)

        return count

    def kthSmallest(self, matrix, k):
        n = len(matrix)
        m = len(matrix[0])

        l = matrix[0][0]
        r = matrix[n - 1][m - 1]
        ans = -1

        while l <= r:
            mid = l + (r - l) // 2

            count = self.countOfSmallerOrEqualElements(matrix, mid)

            if count >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans