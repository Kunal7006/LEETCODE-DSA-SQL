class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        count =0
        ans =""

        for ch in s:
            if ch =="(":
                count+=1
                if count>1: # for outer most open parenthesis
                    ans += ch
            else:
                count-=1
                if count>0: # for outer most close paranthesis
                    ans+=ch
        return ans