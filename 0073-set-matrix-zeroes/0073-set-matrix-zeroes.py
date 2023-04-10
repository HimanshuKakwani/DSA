class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M,N = len(matrix), len(matrix[0])
        row,col = [1]*M, [1]*N

        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    row[r] = 0
                    col[c] = 0

        for r in range(M):
            if row[r] == 0:
                matrix[r] = [0]*N
    
        for c in range(N):
            if col[c] == 0:
                for i in range(M):
                    matrix[i][c] = 0
                
        return matrix

        