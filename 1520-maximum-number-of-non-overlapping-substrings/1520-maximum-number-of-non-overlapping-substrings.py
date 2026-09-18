class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        start = [-1] * 26
        end = [0] * 26
        isValid = [True] * 26

        result =[]

        for i in range(n):
            idx = ord(s[i]) - ord('a')

            if start[idx] == -1:
                start[idx]=i
            end[idx]=i
        
        for c in range(26):
            if start[c]==-1:
                continue

            i = start[c]

            while i <= end[c]:
                curr = ord(s[i]) - ord('a')

                if start[curr] < start[c]:
                    isValid[c] = False
                    break

                end[c] = max(end[c], end[curr])

                i += 1
        
        lastTakenStart = float('inf')

        for i in range(n-1,-1,-1):
            c = ord(s[i])-ord('a')

            if  not isValid[c]:
                continue
            
            if i == start[c]  and end[c]<lastTakenStart:
                result.append(s[i:end[c]+1])
                lastTakenStart =i
        
        return result

