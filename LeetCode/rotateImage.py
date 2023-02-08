class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #layers
        for i in range(0, len(matrix)//2):
            for j in range(i, len(matrix)-1-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[len(matrix)-1-j][i]
                matrix[len(matrix)-1-j][i] = matrix[len(matrix)-1-i][len(matrix)-1-j]
                matrix[len(matrix)-1-i][len(matrix)-1-j] = matrix[j][len(matrix)-1-i]
                matrix[j][len(matrix)-1-i] = temp
        return matrix