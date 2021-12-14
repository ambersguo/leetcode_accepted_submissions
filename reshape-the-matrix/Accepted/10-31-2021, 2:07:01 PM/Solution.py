// https://leetcode.com/problems/reshape-the-matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat_list = []
        mat_reshape = []
        if m*n == r*c:
            for i in range(m):
                for j in range(n):
                    mat_list.append(mat[i][j])
            for i in range(0, len(mat_list), c):
                mat_reshape.append(mat_list[i:i+c])
        else:
            mat_reshape = mat
        return mat_reshape
