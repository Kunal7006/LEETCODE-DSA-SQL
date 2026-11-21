class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom up 
        m = len(text1)
        n = len(text2)

        t=[[0]*(n+1) for _ in range(m+1)]

        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j]= max(t[i][j-1],t[i-1][j])
        return t[m][n]