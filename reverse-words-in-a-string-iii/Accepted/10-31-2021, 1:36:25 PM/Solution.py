// https://leetcode.com/problems/reverse-words-in-a-string-iii

import re
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = re.split(' ', s)
        s_new_list = []
        s_new = ""
        for s_ele in s_list:
            s_rev = s_ele[::-1]
            s_new_list.append(s_rev)
        s_new = ' '.join(s_new_list)
        return s_new
