class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count =[0]*26

        for ch in s:
            count[ord(ch)-ord('a')]+=1
            if count[ord(ch)-ord('a')] > (n+1)//2:
                return ""
        
        heap =[]

        for i in range(26):
            if count[i] > 0:
                ch = chr(i + ord('a'))
                heapq.heappush(heap, (-count[i], ch))
        
        result = ""

        while len(heap) >= 2:
            P1 = heapq.heappop(heap)
            P2 = heapq.heappop(heap)

            result += P1[1]
            result += P2[1]

            freq1 = P1[0] + 1
            freq2 = P2[0] + 1

            if freq1 < 0:
                heapq.heappush(heap, (freq1, P1[1]))

            if freq2 < 0:
                heapq.heappush(heap, (freq2, P2[1]))

        if heap:
            result += heapq.heappop(heap)[1]

        return result
