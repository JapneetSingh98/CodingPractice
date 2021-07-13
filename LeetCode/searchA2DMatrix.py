class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        for row in range(1, len(matrix)):
            print(row)
            if matrix[row][0] > target:
                return target in matrix[row-1]
            else:
                continue
        print(row)
        return target in matrix[row]