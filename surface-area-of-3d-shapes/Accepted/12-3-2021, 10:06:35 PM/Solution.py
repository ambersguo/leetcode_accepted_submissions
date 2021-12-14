// https://leetcode.com/problems/surface-area-of-3d-shapes

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        area = 0
        for i in range(n):
            pre_j = -1
            for j in range(m):
                if grid[i][j]:
                    area += grid[i][j]*6 - (grid[i][j]-1)*2
                if pre_j >= 0:
                    area -= min(grid[i][j], grid[i][pre_j])*2 
                pre_j = j
        
        for j in range(m):
            pre_i = -1
            for i in range(n):
                if pre_i >= 0:
                    area -= min(grid[i][j], grid[pre_i][j])*2
                pre_i = i
        return area
