class Solution:
    def isPalindrome(self,s,low,high):
        while low<high:
            if s[low]!=s[high]:
                return False
            low+=1
            high-=1
        return True
    def backtrack(self,index,s,result,curr):
        if index == len(s):
            result.append(curr.copy())
            return
        
        for i in range(index,len(s)):
            if self.isPalindrome(s,index,i):
                curr.append(s[index:i+1])
                self.backtrack(i+1,s,result,curr)
                curr.pop()

    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        result =[]
        curr =[]

        self.backtrack(0,s,result,curr)
        return result