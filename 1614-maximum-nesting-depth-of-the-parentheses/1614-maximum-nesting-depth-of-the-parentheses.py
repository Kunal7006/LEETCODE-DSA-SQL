class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        count =0
        maxDepth =0

        for i in range(n):
            if s[i]=='(':
                count+=1
                maxDepth = max(maxDepth,count)
            elif s[i]==')':
                count-=1
            else:
                continue
        return maxDepth