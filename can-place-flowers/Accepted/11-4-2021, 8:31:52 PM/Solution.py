// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count0 = total = i = 0
        counts = []
        for f in flowerbed:
            if f == 0:
                if i == 0:
                    if len(flowerbed) == 1:
                        count0 += 3
                        counts.append(count0)
                    else:
                        count0 += 2
                elif i == len(flowerbed) - 1:
                    count0 += 2
                    counts.append(count0)
                else:
                    count0 += 1
            else:
                if count0:
                    counts.append(count0)
                    count0 = 0
            i += 1
        for c in counts:
            if c%2 == 0:
                total += (c-2)/2
            else:
                total += (c-1)/2
        if n > int(total):
            return False
        else:
            return True
