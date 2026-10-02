class Solution:
    def solve(self,ans,n,oc,cc,temp):
        if oc == n and cc == n:
            ans.append(temp)
        
        if oc < n:
            self.solve(ans,n,oc+1,cc,temp+'(')
        if cc< oc:
            self.solve(ans,n,oc,cc+1,temp+')')
        
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        oc =0
        cc=0
        temp =""

        self.solve(ans,n,oc,cc,temp)

        return ans

       
