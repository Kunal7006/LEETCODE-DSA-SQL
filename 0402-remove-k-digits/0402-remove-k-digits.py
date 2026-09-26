class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []

        for i in range(n):
            while stack and k>0 and ord(stack[-1])-ord('0')> ord(num[i])-ord('0'):
                stack.pop()
                k-=1
            stack.append(num[i])
        
        while k >0:
            stack.pop()
            k-=1
        
        if not stack:
            return "0"
        
        res =""

        while stack:
            res += stack[-1]
            stack.pop()
        
        while len(res)!=0 and res[-1]=='0':
            res = res[:-1]

        res = res[::-1]
        if not res:
            return "0"
        return res