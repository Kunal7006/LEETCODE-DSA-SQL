class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        rDegree =0

        for i in range(1,n+1):
            product = (26 - (ord(s[i-1]) - ord('a'))) * i

            rDegree += product
        return rDegree