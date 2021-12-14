// https://leetcode.com/problems/add-strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_len = len(num1)
        num2_len = len(num2)
        if num1_len > num2_len:
            long = num1_len
            short = num2_len
            long_num = num1[:]
        else:
            long = num2_len
            short = num1_len
            long_num = num2[:]
        num1_r = num1[::-1]
        num2_r = num2[::-1]
        long_num_r = long_num[::-1]
        s = ""
        check = 0
        for i in range(long):
            if i < short:
                num = int(num1_r[i]) + int(num2_r[i])
                if check:
                    num += 1
                if num < 10:
                    s = s + str(num)
                    check = 0
                else:
                    s = s + str(num-10)
                    check += 1
            else:
                if check:
                    if int(long_num_r[i]) < 9:
                        s = s + str(int(long_num_r[i]) + 1)
                        check = 0
                    else:
                        s = s + "0"
                        check = 1
                else:
                    s = s + long_num_r[i]
                    check = 0
        if check:
            s = s + "1"
        s_s = s[::-1]
        return s_s
