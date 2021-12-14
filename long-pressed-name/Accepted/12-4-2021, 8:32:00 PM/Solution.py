// https://leetcode.com/problems/long-pressed-name

from collections import defaultdict

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_list = list(name)
        typed_list = list(typed)
        name_seen = set()
        typed_seen = set()
        name_uniq = []
        typed_uniq = []
        pre_c = ''
        name2count = defaultdict(int)
        typed2count = defaultdict(int)
        namec2order = defaultdict(int)
        typedc2order = defaultdict(int)
        nameuniqorder = defaultdict(int)

        for i in range(len(name_list)):
            c = name_list[i]
            if c not in name_seen:
                name_seen.add(c)
                name_uniq.append(c)
                namec2order[c] += 1
            else:
                if pre_c != c:
                    name_uniq.append(c)
                    namec2order[c] += 1
            co = c + str(namec2order[c])
            name2count[co] += 1
            pre_c = c

        for i in range(len(typed_list)):
            c = typed_list[i]
            if c not in typed_seen:
                typed_seen.add(c)
                typed_uniq.append(c)
                typedc2order[c] += 1
            else:
                if pre_c != c:
                    typed_uniq.append(c)
                    typedc2order[c] += 1
            co = c + str(typedc2order[c])
            typed2count[co] += 1
            pre_c = c

        if name_uniq == typed_uniq:
            if len(name_uniq) == len(name_list):
                return True
            else:
                for c in name_uniq:
                    
                    name2count[c] += 1
                for c in typed:
                    typed2count[c] += 1
                for c in name_uniq:
                    nameuniqorder[c] += 1
                    co = c + str(nameuniqorder[c])
                    if typed2count[co] < name2count[co]:
                        return False
                return True       
        else:
            return False
