class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        freq =[0]*256
        minLength = float('inf')
        count = 0

        for i in range(m):
            freq[ord(t[i])]+=1
        
        l=0
        r=0
        sIndex =-1

        while r<n :
            if freq[ord(s[r])] > 0:
                count+=1
            
            freq[ord(s[r])]-=1

            while count == m:
                if r-l+1 <minLength:
                    minLength = r-l+1
                    sIndex = l  
                
                freq[ord(s[l])]+=1

                if freq[ord(s[l])] >0:
                    count-=1
                
                l+=1
            r+=1
        
        if sIndex == -1:
            return ""
        
        return s[sIndex:sIndex + minLength]


        