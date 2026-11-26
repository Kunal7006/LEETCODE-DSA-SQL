class Solution:
    def canAliceWin(self, n: int) -> bool:
        flag = False
        if n<10:
            return flag
        
        last =10
        n = n-last
        flag = True
        while n>=last-1:
            flag = not flag
            last = last -1
            n = n-last
        return flag