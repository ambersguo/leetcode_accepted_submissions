// https://leetcode.com/problems/minimum-index-sum-of-two-lists

from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res2index1 = {}
        res2index2 = {}
        common = []
        sums = []
        least = []
        sumindice2res = defaultdict(list)
        for i in range(len(list1)):
            res2index1[list1[i]] = i
        for i in range(len(list2)):
            res2index2[list2[i]] = i
            if list2[i] in res2index1.keys():
                common.append(list2[i])
        for res in common:
            sum_indice = res2index1[res] + res2index2[res]
            sums.append(sum_indice)
            sumindice2res[sum_indice].append(res)
        sums.sort()
        return sumindice2res[sums[0]]
