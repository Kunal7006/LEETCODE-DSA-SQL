class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]

        for token in path.split('/'):
            if token =="" or token ==".":
                continue
            if token != "..":
                stack.append(token)
            elif stack:
                stack.pop()

        if not stack:
            return "/"
        
        result =""

        while(stack):
            result = "/"+stack[-1]+result
            stack.pop()
        
        return result