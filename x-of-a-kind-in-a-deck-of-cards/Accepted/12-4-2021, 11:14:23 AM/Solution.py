// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards

from collections import defaultdict

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        values = []
        n2count = defaultdict(int)
        for n in deck:
            n2count[n] += 1
        value_list = list(set(n2count.values()))
        value_list.sort()
        for v in value_list:
            values.append(str(v))
        if len(value_list) == 1:
            if '1' in values:
                return False
            elif '0' in values:
                return False
            else:
                return True
        else:
            for n in range(2, value_list[0]+1):
                count = 0
                for v in value_list:
                    if v%n == 0:
                        count += 1
                if count == len(value_list):
                    return True
            return False

