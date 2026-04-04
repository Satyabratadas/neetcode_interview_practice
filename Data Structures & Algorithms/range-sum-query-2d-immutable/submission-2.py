class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # ROWS, COLS = len(matrix), len(matrix[0])
        # self.sum_mat = [[0] * (COLS+1) for r in range (ROWS+1)]
        # for r in range(ROWS):
        #     prefix = 0
        #     for c in range(COLS):
        #         prefix += matrix[r][c]
        #         above = self.sum_mat[r][c + 1]
        #         self.sum_mat[r+1][c+1] = prefix + above
        self.mat_sum = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        # bottomright = self.sum_mat[r2][c2]
        # above = self.sum_mat[r1 - 1][c2]
        # left = self.sum_mat[r2][c1 - 1]
        # top_left = self.sum_mat[r1 - 1] [c1 - 1]
        # return bottomright - above - left + top_left
        total = 0
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                total += self.mat_sum[r][c]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)