// https://leetcode.com/problems/self-dividing-numbers

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        num = left
        self_div_nums = []
        while num <= right:
            if num%10 == 0:
                next
            else:
                check = 1
                for n in str(num):
                    if int(n) == 0:
                        check = 0
                        break
                    else:
                        if num%int(n) != 0:
                            check = 0
                            break
                if check:
                    self_div_nums.append(num)
            num += 1
        return self_div_nums
