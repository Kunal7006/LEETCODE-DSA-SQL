class Solution:
    class Node:
        def __init__(self):
            self.score = -1
            self.idxs = []

    def __init__(self):
        self.n = 0
        self.nextIdx = []
        self.t = []

    def findNext(self, intervals, r):
        lo = 0
        hi = self.n - 1
        result = self.n

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if intervals[mid][0] > r:
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return result

    def solve(self, intervals, i, k):
        if k == 0 or i >= self.n:
            return self.Node()

        if self.t[i][k].score != -1:
            return self.t[i][k]

        # Skip current interval
        skip = self.solve(intervals, i + 1, k)

        # Take current interval
        weight = intervals[i][2]
        idx = intervals[i][3]
        j = self.nextIdx[i]

        temp = self.solve(intervals, j, k - 1)

        take = self.Node()
        take.score = temp.score + weight
        take.idxs = temp.idxs.copy()
        take.idxs.append(idx)

        take.idxs.sort()

        # Choose better result
        if skip.score > take.score:
            result = skip
        elif skip.score < take.score:
            result = take
        else:
            # Lexicographically smaller indices
            if skip.idxs < take.idxs:
                result = skip
            else:
                result = take

        self.t[i][k] = result
        return result

    def maximumWeight(self, intervals):
        self.n = len(intervals)

        # Add original index
        for i in range(self.n):
            intervals[i].append(i)

        # Sort by interval values
        intervals.sort()

        # Calculate next non-overlapping interval
        self.nextIdx = [0] * self.n

        for i in range(self.n):
            end = intervals[i][1]
            self.nextIdx[i] = self.findNext(intervals, end)

        K = 4

        # DP table
        self.t = [
            [self.Node() for _ in range(K + 1)]
            for _ in range(self.n + 1)
        ]

        return self.solve(intervals, 0, K).idxs