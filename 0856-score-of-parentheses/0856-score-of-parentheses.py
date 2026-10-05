class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # without extra space

        n = len(s)
        score =0
        depth =0

        for i in range(n):
            if s[i]=='(':
                depth +=1
            else:
                depth -=1
                if s[i-1]=='(': # simplest unit
                    score += (1<<depth)
        return score