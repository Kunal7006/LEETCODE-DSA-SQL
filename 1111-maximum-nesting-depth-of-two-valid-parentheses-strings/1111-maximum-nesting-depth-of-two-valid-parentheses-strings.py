class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        depth =0
        ans =[]

        for i in range(n):
            if seq[i]=='(':
                depth+=1
                ans.append(depth % 2)
            if seq[i]==')':
                ans.append(depth % 2)
                depth -=1
        return ans 