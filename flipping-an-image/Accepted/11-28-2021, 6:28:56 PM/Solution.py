// https://leetcode.com/problems/flipping-an-image

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows_final = []
        for row in image:
            row_final = []
            row_str_rev = ''.join([str(x) for x in row])[::-1]
            for s in row_str_rev:
                if s == '1':
                    n = 0
                else:
                    n = 1
                row_final.append(n)
            rows_final.append(row_final)
        return rows_final
