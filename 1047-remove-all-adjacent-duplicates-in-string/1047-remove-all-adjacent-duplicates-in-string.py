class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        ans =""

        for i in range(n):
            if len(ans)>0 and ans[-1]==s[i]:
                ans = ans[:-1]
            else:
                ans += s[i]
        return ans