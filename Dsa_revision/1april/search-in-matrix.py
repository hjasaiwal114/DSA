class Solution:
    def matSearch(self,matrix, N, M, target):
        row = len(matrix)
        col = len(matrix[0])
        r = 0
        c = col - 1
        while r<row and c>=0:
            if matrix[r][c] == target:
                return 1
            elif matrix[r][c]<target:
                r += 1
            else:
                c -= 1
        return 0