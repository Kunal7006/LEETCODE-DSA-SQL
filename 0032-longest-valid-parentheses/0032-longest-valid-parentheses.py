class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        open =0
        close =0
        result =0

        for i in range(n):
            if s[i]=='(':
                open+=1
            else:
                close+=1

            if close>open:
                open =0
                close =0
            if open == close:
                result = max(result,open + close)
        
        open =0
        close =0

        for i in range(n-1,-1,-1):
            if s[i]=='(':
                open+=1
            else:
                close+=1
            
            if open>close:
                open =0
                close =0
            if open == close:
                result = max(result,open + close)

        return result
