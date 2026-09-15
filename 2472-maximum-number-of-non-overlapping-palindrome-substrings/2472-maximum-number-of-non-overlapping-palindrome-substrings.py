class Solution:
    def check(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans =0
        start =0

        for r in range(k-1,n):
            for ln in range(k,r-start+2):
                l = r-ln +1

                if self.check(s,l,r):
                    ans +=1
                    start = r+1
                    break
        return ans