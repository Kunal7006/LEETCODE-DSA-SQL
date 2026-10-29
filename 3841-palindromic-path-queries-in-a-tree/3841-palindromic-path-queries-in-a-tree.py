
class Solution:
    def dfs(self, node, parent, d, s):
        self.depth[node] = d
        self.ancestorTable[node][0] = parent

        self.tin[node] = self.time
        self.eulerTour[self.time] = (1 << (ord(s[node]) - ord('a')))
        self.time += 1

        for child in self.adj[node]:
            if child == parent:
                continue
            self.dfs(child, node, d + 1, s)

        self.tout[node] = self.time
        self.eulerTour[self.time] = (1 << (ord(s[node]) - ord('a')))
        self.time += 1

    # Segment Tree Build
    def buildSegmentTree(self, i, l, r, nums):
        if l == r:
            self.segmentTree[i] = nums[l]
            return

        mid = l + (r - l) // 2

        self.buildSegmentTree(2 * i + 1, l, mid, nums)
        self.buildSegmentTree(2 * i + 2, mid + 1, r, nums)

        self.segmentTree[i] = (
            self.segmentTree[2 * i + 1] ^
            self.segmentTree[2 * i + 2]
        )

    # Segment Tree Point Update (XOR)
    def updateSegTree(self, index, val, i, l, r):
        if l == r:
            self.segmentTree[i] = val
            return

        mid = l + (r - l) // 2

        if index <= mid:
            self.updateSegTree(index, val, 2 * i + 1, l, mid)
        else:
            self.updateSegTree(index, val, 2 * i + 2, mid + 1, r)

        self.segmentTree[i] = (
            self.segmentTree[2 * i + 1] ^
            self.segmentTree[2 * i + 2]
        )

    # Segment Tree Range Query
    def querySegmentTree(self, start, end, i, l, r):
        if l > end or r < start:
            return 0

        if l >= start and r <= end:
            return self.segmentTree[i]

        mid = l + (r - l) // 2

        return (
            self.querySegmentTree(start, end, 2 * i + 1, l, mid) ^
            self.querySegmentTree(start, end, 2 * i + 2, mid + 1, r)
        )

    # Build Ancestor Table using Binary Lifting
    def buildAncestorTable(self):
        for j in range(1, self.cols):
            for node in range(self.n):
                if self.ancestorTable[node][j - 1] != -1:
                    parent = self.ancestorTable[node][j - 1]
                    self.ancestorTable[node][j] = (
                        self.ancestorTable[parent][j - 1]
                    )

    # Get LCA using Binary Lifting
    def getLCA(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]

        for j in range(self.cols):
            if diff & (1 << j):
                u = self.ancestorTable[u][j]

        if u == v:
            return u

        for j in range(self.cols - 1, -1, -1):
            if self.ancestorTable[u][j] != self.ancestorTable[v][j]:
                u = self.ancestorTable[u][j]
                v = self.ancestorTable[v][j]

        return self.ancestorTable[u][0]

    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:

        self.n = n
        self.adj = [[] for _ in range(n)]

        for edge in edges:
            u = edge[0]
            v = edge[1]

            self.adj[u].append(v)
            self.adj[v].append(u)

        self.tin = [0] * n
        self.tout = [0] * n
        self.depth = [0] * n
        self.eulerTour = [0] * (2 * n)

        self.time = 0
        self.cols = n.bit_length()

        self.ancestorTable = [
            [-1] * self.cols for _ in range(n)
        ]

        # Python strings are immutable
        s = list(s)

        # DFS from root 0
        self.dfs(0, -1, 0, s)

        # Build Segment Tree
        N = 2 * n
        self.segmentTree = [0] * (4 * N)

        self.buildSegmentTree(0, 0, N - 1, self.eulerTour)

        # Build Binary Lifting Table
        self.buildAncestorTable()

        result = []

        for q in queries:
            parts = q.split()
            type = parts[0]

            if type == "update":
                node = int(parts[1])
                c = parts[2]

                charValue = (1 << (ord(c) - ord('a')))
                s[node] = c

                self.updateSegTree(
                    self.tin[node], charValue, 0, 0, 2 * n - 1
                )

                self.updateSegTree(
                    self.tout[node], charValue, 0, 0, 2 * n - 1
                )

            else:
                u = int(parts[1])
                v = int(parts[2])

                lcaNode = self.getLCA(u, v)

                ch = s[lcaNode]
                charValue = (1 << (ord(ch) - ord('a')))

                mask = (
                    self.querySegmentTree(
                        0, self.tin[u], 0, 0, 2 * n - 1
                    ) ^
                    self.querySegmentTree(
                        0, self.tin[v], 0, 0, 2 * n - 1
                    ) ^
                    charValue
                )

                result.append((mask & (mask - 1)) == 0)

        return result
