// https://leetcode.com/problems/projection-area-of-3d-shapes

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        total = 0
        
        for i in range(n):
            row = []
            for j in range(m):
                row.append(grid[i][j])
                if grid[i][j]:
                    total += 1
            total += max(row)
        
        for j in range(m):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            total += max(col)
            
        return total
