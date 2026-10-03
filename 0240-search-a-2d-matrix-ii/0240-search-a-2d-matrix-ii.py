class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        rowIndex = 0
        colIndex = col -1

        while rowIndex < row and colIndex>=0:
            element = matrix[rowIndex][colIndex]

            if element == target:
                return True
            if element> target:
                colIndex-=1
            else:
                rowIndex+=1
        return False