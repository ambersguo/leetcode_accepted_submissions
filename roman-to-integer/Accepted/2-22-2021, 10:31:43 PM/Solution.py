// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        s_test = s
        sum = 0
        for key in special_dict:
            if key in s_test:
                key_count = len(s_test.split(key)) -1
                sum = sum + key_count * special_dict.get(key, 0)
                s_test = ''.join(s_test.split(key))
            else:
                next
                
        s_list = list(s_test)
        for n in s_list:
            sum = sum + roman_dict.get(n, 0)
        return sum  
