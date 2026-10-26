class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:

        if m*n != len(original):
            return []
        x = 0
        mat = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                mat[i][j] = original[x]
                x += 1

        return mat

        