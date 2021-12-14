// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
            n = 0
            list1 = [1]
            list2 = []
            while n < rowIndex + 1:
                pre = 0
                list2 = []
                if n > 0:
                    for value in list1:
                        new_value = pre + value
                        pre = value
                        list2.append(new_value)
                    list2.append(1)
                    list1 = list2
                if rowIndex == 0:
                    return list1
                elif n == rowIndex:
                    return list2
                n = n+1
