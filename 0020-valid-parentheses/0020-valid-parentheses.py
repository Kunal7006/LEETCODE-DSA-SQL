class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        n = len(s)

        for i in range(n):
            ch = s[i]
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)
            elif stack:
                if stack[-1]=='(' and s[i]==')' or stack[-1]=='{' and s[i]=='}' or stack[-1]=='[' and s[i]==']':
                    stack.pop()
                else:
                    return False
            else:
                return False
            
        if not stack:
            return True
        else:
            return False