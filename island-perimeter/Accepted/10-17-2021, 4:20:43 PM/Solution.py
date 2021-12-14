// https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        pre_indice = []
        indice = []
        for row in grid:
            indice = []
            count = 0
            minus = 0
            pre_i = -1000
            for i in range(len(row)):  
                if row[i] == 1:
                    indice.append(i)
                    count += 1
                    if i-pre_i == 1:
                        minus += 1
                    pre_i = i
            for index in indice:
                if index in pre_indice:
                    minus += 1
            perimeter = perimeter + count*4 - minus*2
            print(perimeter)
            pre_indice = indice[:]
        return perimeter   
