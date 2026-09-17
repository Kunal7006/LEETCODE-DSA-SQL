class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        i = 0
        j = 0

        bestMinLenTillIdx = [float("inf")] * n
        currSum = 0
        bestMinLen = float("inf")
        result = float("inf")

        while j < n:
            currSum += arr[j]
            while i < j and currSum > target:
                currSum -= arr[i]
                i += 1

            if currSum == target:
                ln = j - i + 1
                if i > 0 and bestMinLenTillIdx[i - 1] != float("inf"):
                    result = min(result, ln + bestMinLenTillIdx[i - 1])

                bestMinLen = min(bestMinLen, ln)

            bestMinLenTillIdx[j] = bestMinLen

            j += 1
        if result == float("inf"):
            return -1
        return result
