// https://leetcode.com/problems/binary-gap

class Solution:
    def binaryGap(self, n: int) -> int:
        n_bin = format(n,'b')
        check = 0
        distance = []
        for i in range(len(n_bin)):
            if n_bin[i] == '1':
                if not check:
                    left = i
                    check = 1
                else:
                    right = i
                    distance.append(right-left)
                    left = i
        distance.sort(reverse=True)
        if distance:
            return distance[0]
        else:
            return 0
