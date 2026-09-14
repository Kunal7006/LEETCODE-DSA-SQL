class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        deq = deque()  # stores indices in monotonic increasing order of cumulative sum

        cumulativeSum = [0] * n  # stores cumulative sum

        result = float('inf')  # equivalent to INT_MAX

        j = 0

        while j < n:

            if j == 0:
                cumulativeSum[j] = nums[j]
            else:
                cumulativeSum[j] = cumulativeSum[j - 1] + nums[j]

            # subarray starting from index 0
            if cumulativeSum[j] >= k:
                result = min(result, j + 1)

            # Try to shrink the window from the front
            while (deq and
                   cumulativeSum[j] - cumulativeSum[deq[0]] >= k):

                result = min(result, j - deq[0])

                deq.popleft()

            # Remove useless prefix sums from the back
            while (deq and
                   cumulativeSum[j] <= cumulativeSum[deq[-1]]):

                deq.pop()

            deq.append(j)

            j += 1

        return -1 if result == float('inf') else result