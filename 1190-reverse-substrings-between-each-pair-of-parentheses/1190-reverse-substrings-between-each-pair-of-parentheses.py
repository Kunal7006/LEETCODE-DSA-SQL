class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack =[]
        curr =""

        for i in range(n):
            if s[i]=='(':
                stack.append(curr)
                curr =""
            elif s[i]==')':
                curr = curr[::-1]
                curr = stack[-1]+curr
                stack.pop()
            else:
                curr += s[i]
        return curr
                
