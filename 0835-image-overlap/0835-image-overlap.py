class Solution:
    def countOverlaps(self,A,B,rowOff,colOff):
        n = len(A)
        count =0

        for i in range(n):
            for j in  range(n):
                B_i = i+rowOff
                B_j = j+colOff

                if B_i <0 or B_i>=n or B_j <0 or B_j >=n:
                    continue
                
                if A[i][j]==1 and B[B_i][B_j]==1:
                    count +=1
        return count


    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)

        maxOverlaps =0

        for rowOff in range(-n+1,n):
            for colOff in range(-n+1,n):

                count = self.countOverlaps(A,B,rowOff,colOff)

                maxOverlaps = max(maxOverlaps,count)
        
        return maxOverlaps