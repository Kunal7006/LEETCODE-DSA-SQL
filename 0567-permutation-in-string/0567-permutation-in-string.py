class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        s1_freq = [0]* 26
        s2_freq = [0] * 26

        if n > m :
            return False

        for i in range(n):
            s1_freq[ord(s1[i]) - ord('a')] +=1
        
        l =0
        r=0

        while r< m:
            s2_freq[ord(s2[r])-ord('a')]+=1

            if r-l+1 > n:
                s2_freq[ord(s2[l]) - ord('a')]-=1
                l+=1

            if s1_freq == s2_freq:
                return True
            
            r+=1
        
        return False
            
        