// https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_dict = dict()
        for i in range (0,len(nums)):
            nums_dict[nums[i]]= i
        target_loci = 0
        if nums_dict.get(target):
            target_loci = nums_dict[target]
        else:
            while target > nums[0]:
                target = target -1
                if nums_dict.get(target) or nums_dict.get(target) == 0 :
                    target_loci = nums_dict.get(target) + 1
                    break
                else:
                    next
        return target_loci
 