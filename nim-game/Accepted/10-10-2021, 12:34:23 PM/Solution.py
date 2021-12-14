// https://leetcode.com/problems/nim-game

class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 == 0:
            return False
        elif n%6 == 0:
            n = 6
        elif n > 12:
            n = n%12
        nlist = [n] 
        nblist = []
        check = 0
        while nlist:
            for n in nlist:
                nlist.remove(n)
                for a in [1,2,3]:
                    check = 0
                    n_a = n
                    n_a = n-a
                    if n_a == 0:
                        return True
                    for b in [1,2,3]:
                        n_b = n_a
                        n_b = n_a-b
                        if n_b == 0:
                            check+=1
                            next
                        else:
                            nblist.append(n_b)
                    if not check:
                        nlist = nlist + nblist
                    nblist = []
        return False
