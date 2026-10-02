class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        start =0
        end = row * col -1

        while start<= end:
            mid = start + (end - start)//2

            element = matrix[mid//col][mid%col]

            if element == target:
                return True
            if element > target:
                end = mid -1
            else:
                start = mid +1
        return False