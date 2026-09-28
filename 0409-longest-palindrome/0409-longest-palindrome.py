class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        mp={}

        for i in range(n):
            if s[i] not in mp:
                mp[s[i]]=0
            mp[s[i]]+=1

        result =0
        oddFreq = False

        for key,value in mp.items():
            if value % 2 ==0:
                result += value
            else:
                result += value -1
                oddFreq = True
        if oddFreq:
            result+=1
        return result