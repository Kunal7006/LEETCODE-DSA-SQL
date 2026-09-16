class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        n = len(firstList)
        m = len(secondList)
        ans =[]
        first =0
        second =0

        while first < n and second < m:
            if firstList[first][0]<=secondList[second][1] and firstList[first][1]>=secondList[second][0]:
                temp=[0]*2
                temp[0]= max(firstList[first][0],secondList[second][0])
                temp[1]= min(firstList[first][1],secondList[second][1])
                ans.append(temp)
            if firstList[first][1]<secondList[second][1]:
                first+=1
            else:
                second+=1
        return ans