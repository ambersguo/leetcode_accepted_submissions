// https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums_len = len(nums)
        output = []
        i = 0
        if nums:
            start = nums[0]
            while i < nums_len-1:
                if nums[i+1] - nums[i] == 1:
                    i+=1
                    next
                else:
                    if start == nums[i]:
                        ele = str(start)
                    else:
                        ele = str(start) + "->" + str(nums[i])
                    output.append(ele)
                    start = nums[i+1]
                    i+=1
            if start == nums[-1]:
                output.append(str(start))
            else:
                ele = str(start) + "->" + str(nums[i])
                output.append(ele)
            return output
        else:
            return nums
