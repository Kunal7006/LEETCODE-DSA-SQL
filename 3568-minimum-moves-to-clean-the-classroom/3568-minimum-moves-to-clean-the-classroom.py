from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        startR = 0
        startC = 0

        # Give every litter an ID
        litterId = [[-1] * n for _ in range(m)]
        litterCount = 0

        for i in range(m):
            for j in range(n):

                if classroom[i][j] == 'S':
                    startR = i
                    startC = j

                if classroom[i][j] == 'L':
                    litterId[i][j] = litterCount
                    litterCount += 1

        finalMask = (1 << litterCount) - 1

        # State:
        # (row, col, energy, mask, distance)
        q = deque()

        q.append((startR, startC, energy, 0, 0))

        # visited[row][col][energy][mask]
        visited = set()

        visited.add((startR, startC, energy, 0))

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q:

            r, c, currEnergy, mask, dist = q.popleft()

            # All litter collected
            if mask == finalMask:
                return dist

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # No energy to make a move
                if currEnergy == 0:
                    continue

                newEnergy = currEnergy - 1
                newMask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    litter = litterId[nr][nc]
                    newMask |= (1 << litter)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    newEnergy = energy

                state = (nr, nc, newEnergy, newMask)

                if state not in visited:

                    visited.add(state)

                    q.append((
                        nr,
                        nc,
                        newEnergy,
                        newMask,
                        dist + 1
                    ))

        return -1