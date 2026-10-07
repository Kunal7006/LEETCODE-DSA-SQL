class Solution:
    def __init__(self):
        self.n = 0
        self.st = set()
        self.maxLen = 0

    def solve(self, s, i, curr, count):
        if count < 0:
            return

        if i == self.n:
            if count == 0:
                if len(curr) > self.maxLen:
                    self.maxLen = len(curr)
                    self.st.clear()

                if len(curr) == self.maxLen:
                    self.st.add(''.join(curr))

            return

        if s[i] != '(' and s[i] != ')':
            curr.append(s[i])
            self.solve(s, i + 1, curr, count)
            curr.pop()
            return

        curr.append(s[i])

        self.solve(
            s,
            i + 1,
            curr,
            count + (1 if s[i] == '(' else -1)
        )

        curr.pop()

        self.solve(s, i + 1, curr, count)

    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.n = len(s)
        self.st.clear()
        self.maxLen = 0

        curr = []
        self.solve(s, 0, curr, 0)

        return list(self.st)