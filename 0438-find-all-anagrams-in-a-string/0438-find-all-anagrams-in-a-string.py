class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)

        sIndex = -1
        ans =[]

        sFreq = [0] * 26
        pFreq = [0] * 26 

        for i in range(n):
            pFreq[ord(p[i]) - ord('a')] +=1
        
        l=0
        r=0

        while r < m:
            sFreq[ord(s[r]) - ord('a')] +=1

            if r-l+1 > n:
                sFreq[ord(s[l])-ord('a')] -=1
                l+=1
            
            if sFreq == pFreq:
                ans.append(l)
            
            r+=1
        
        return ans
