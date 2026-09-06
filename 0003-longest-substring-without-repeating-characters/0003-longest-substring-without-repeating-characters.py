class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        last = [-1]*256
        l=0
        r=0
        maxLength =0

        while r<n:
            index = ord(s[r])
            if last[index]!=-1:
                if last[index]>=l:
                    l=last[index]+1
            
            last[index]=r
            maxLength = max(maxLength,r-l+1)
            r+=1
        
        return maxLength