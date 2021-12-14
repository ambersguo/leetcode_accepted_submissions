// https://leetcode.com/problems/maximum-product-of-three-numbers

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums_neg = []
        nums_pos = []
        for num in nums:
            if num >= 0:
                nums_pos.append(num)
            else:
                nums_neg.append(num)
        nums_pos.sort(reverse=True)
        nums_neg.sort()
        if len(nums_pos) >= 3:
            max_pos = nums_pos[0]*nums_pos[1]*nums_pos[2]
            if len(nums_neg) >= 2:
                max_mix = nums_neg[0]*nums_neg[1]*nums_pos[0]
                if max_pos > max_mix:
                    return max_pos
                else:
                    return max_mix
            else:
                return max_pos
        elif len(nums_pos) == 2:
            if len(nums_neg) >= 2:
                max_mix = nums_neg[0]*nums_neg[1]*nums_pos[0]
                return max_mix
            else:
                max_mix = nums_pos[0]*nums_pos[1]*nums_neg[-1]
                return max_mix
        elif len(nums_pos) == 1:
            max_mix = nums_pos[0]*nums_neg[0]*nums_neg[1]
            return max_mix
        else:
            max_neg = nums_neg[-1]*nums_neg[-2]*nums_neg[-3]
            return max_neg
