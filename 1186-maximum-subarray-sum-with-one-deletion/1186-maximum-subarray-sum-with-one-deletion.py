class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        ans = arr[0]
        noDelete = arr[0]
        oneDelete = float('-inf')

        for i in range(1,n):

            prevNoDelete = noDelete

            noDelete = max(noDelete + arr[i],arr[i])

            if oneDelete == float('-inf'):
                oneDelete = prevNoDelete
            else:
                oneDelete = max(oneDelete+arr[i],prevNoDelete)
            
            ans = max(ans,max(oneDelete,noDelete))
        return ans 