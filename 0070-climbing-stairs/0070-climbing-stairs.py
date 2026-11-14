class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==0 or n ==1 or n ==2:
            return n
        
        t =[0]*(n+1)
        t[0]=0
        t[1]=1
        t[2]=2

        for i in range(3,n+1):
            t[i]=t[i-2]+t[i-1]
        return t[n]