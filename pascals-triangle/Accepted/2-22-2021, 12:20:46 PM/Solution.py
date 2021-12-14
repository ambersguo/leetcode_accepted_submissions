// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
            n = 0
            list1 = [1]
            list2 = []
            while n < numRows:
                if n == 0:
                    yield list1
                else:
                    pre = 0
                    list2 = []
                    if n > 0:
                        for value in list1:
                            new_value = pre + value
                            pre = value
                            list2.append(new_value)
                        list2.append(1)
                        list1 = list2
                    yield list2
                n = n+1
            return 'done'
        
        