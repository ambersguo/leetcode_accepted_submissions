// https://leetcode.com/problems/valid-mountain-array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        check = max_i = 0
        pre_n = arr[0]

        if len(arr) < 3:
            return False
        
        for i in range(len(arr)):
            if arr[i] > pre_n:
                if not check:
                    next
                else:
                    return False
            elif arr[i] == pre_n:
                if i != 0:
                    return False
            else:
                if not check:
                    max_n = pre_n
                    max_i = i - 1
                    check = 1
                    if max_i == 0:
                        return False
                else:
                    if arr[i] >= pre_n:
                        return False
            pre_n = arr[i]
        
        if check:
            return True
        else:
            return False
