// https://leetcode.com/problems/toeplitz-matrix

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        toeplitz = []
        m = len(matrix)
        n = len(matrix[0])
        l = 1
        k = m-1
        high = max(m,n)
        while k > -high and l < n+1:
            diagnals = []
            for j in range(0,l):
                for i in range(0,m):
                    if i-j == k:
                        diagnal = matrix[i][j]
                        diagnals.append(diagnal)
            l += 1
            k -= 1
            toeplitz.append(diagnals)
            
        l = n - 1
        k = 1
        while k < m+1 and l > -high:
            diagnals = []
            for j in range(0,n):
                for i in range(0,k):
                    if j-i == l:
                        diagnal = matrix[i][j]
                        diagnals.append(diagnal)
            l -= 1
            k += 1
            toeplitz.append(diagnals)
        
        for t in toeplitz:
            t_set = set(t)
            if len(t_set) > 1:
                return False
        return True
