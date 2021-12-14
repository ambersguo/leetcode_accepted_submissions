// https://leetcode.com/problems/reverse-string-ii

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        k2 = k*2
        s_new = ""
        if len(s) > k2:
            s_list = [ s[i:i+k2] for i in range(0, len(s), k2) ]
            for s_ele in s_list:
                if len(s_ele) > k:
                    s_ele_rev = s_ele[0:k][::-1]
                    s_ele_new = s_ele_rev + s_ele[k:]
                else:
                    s_ele_new = s_ele[::-1]
                s_new += s_ele_new
        elif len(s) <= k2 and len(s) > k:
            s_rev = s[0:k][::-1]
            s_new = s_rev + s[k:]
        else:
            s_new = s[::-1]
        return s_new
