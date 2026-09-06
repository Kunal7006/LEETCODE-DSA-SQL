class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        last = [0]* 26
        l=0
        r=0
        maxLength =0
        maxFreq = 0

        while r < n :
            last[ord(s[r])-ord('A')]+=1
            maxFreq = max(maxFreq,last[ord(s[r])-ord('A')])

            if (r-l+1)-maxFreq >k:
                last[ord(s[l])-ord('A')]-=1
                l+=1
            if (r-l+1)-maxFreq <=k:
                maxLength = max(maxLength,r-l+1)
            r+=1
        return maxLength