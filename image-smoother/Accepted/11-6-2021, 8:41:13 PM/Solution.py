// https://leetcode.com/problems/image-smoother

import math
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        smo = [x[:] for x in img]
        if m == 1:
            if n == 1:
                return img
            else:
                for j in range(n):
                    if j == 0:
                        smo[0][j] = math.floor((img[0][j] + img[0][j+1])/2)
                    elif j == n-1:
                        smo[0][j] = math.floor((img[0][j] + img[0][j-1])/2)
                    else:
                        smo[0][j] = math.floor((img[0][j] + img[0][j-1] + img[0][j+1])/3)
                return smo
        elif n == 1:
            for i in range(m):
                if i == 0:
                    smo[i][0] = math.floor((img[i][0] + img[i+1][0])/2)
                elif i == m-1:
                    smo[i][0] = math.floor((img[i][0] + img[i-1][0])/2)
                else:
                    smo[i][0] = math.floor((img[i][0] + img[i+1][0] + img[i-1][0])/3)
            return smo
        else:
            for i in range(m):
                for j in range(n):
                    if j == 0:
                        if i == 0:
                            smo[i][j] = math.floor((img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1])/4)
                        elif i == m-1:
                            smo[i][j] = math.floor((img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1])/4)
                        else:
                            smo[i][j] = math.floor((img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1] + img[i+1][j] + img[i+1][j+1])/6)
                    elif j == n-1:
                        if i == 0:
                            smo[i][j] = math.floor((img[i][j] + img[i][j-1] + img[i+1][j] + img[i+1][j-1])/4)
                        elif i == m-1:
                            smo[i][j] = math.floor((img[i][j] + img[i][j-1] + img[i-1][j] + img[i-1][j-1])/4)
                        else:
                            smo[i][j] = math.floor((img[i][j] + img[i][j-1] + img[i-1][j] + img[i-1][j-1] + img[i+1][j] + img[i+1][j-1])/6)
                    else:
                        if i == 0:
                            smo[i][j] = math.floor((img[i][j] + img[i][j+1] + img[i][j-1] + img[i+1][j] + img[i+1][j-1] + img[i+1][j+1])/6)
                        elif i == m-1:
                            smo[i][j] = math.floor((img[i][j] + img[i][j+1] + img[i][j-1] + img[i-1][j] + img[i-1][j-1] + img[i-1][j+1])/6)
                        else:
                            smo[i][j] = math.floor((img[i][j] + img[i][j-1] + img[i-1][j] + img[i-1][j-1] + img[i+1][j] + img[i+1][j-1] + img[i-1][j+1] + img[i+1][j+1] + img[i][j+1])/9)
            return smo
