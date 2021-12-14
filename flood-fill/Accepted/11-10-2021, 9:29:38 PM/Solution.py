// https://leetcode.com/problems/flood-fill

class Solution:
    def colorChange(self, image: List[List[int]], sr: int, sc: int, oldColor: int) -> List[list[int]]:
        m = len(image)
        n = len(image[0])
        changes = []
        connectors = [[sr-1,sc], [sr+1, sc], [sr, sc-1], [sr, sc+1]]
        for i_j in connectors:
            i = i_j[0]
            j = i_j[1]
            if i>=0 and i<=m-1 and j>=0 and j<= n-1: 
                if image[i][j] == oldColor:
                    changes.append([i, j])
        return changes

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        if oldColor == newColor:
            return image
        changes = self.colorChange(image, sr, sc, oldColor)

        while changes:
            changes_new = []
            for i_j in changes:
                i = i_j[0]
                j = i_j[1]
                image[i][j] = newColor
                changes_new += self.colorChange(image, i, j, oldColor)
            changes = changes_new
        return image
