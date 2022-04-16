class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum = []
        rowlen = len(matrix)
        if rowlen > 0:
            collen = len(matrix[0])
            for i in range(rowlen + 1):
                self.preSum.append([0] * (collen + 1))
            for i in range(rowlen):
                for j in range(collen):
                    # 完整矩阵 = 左边矩阵 + 上边矩阵 - 左上角矩阵 + 自身
                    self.preSum[i+1][j+1] = self.preSum[i+1][j] + \
                        self.preSum[i][j+1] - self.preSum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 当前矩阵 = 完整矩阵 - 左边矩阵 - 上边矩阵 + 左上角矩阵
        return self.preSum[row2+1][col2+1] - self.preSum[row2+1][col1] - self.preSum[row1][col2+1] + self.preSum[row1][col1]
