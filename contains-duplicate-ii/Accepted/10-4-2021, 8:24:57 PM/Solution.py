// https://leetcode.com/problems/contains-duplicate-ii

from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index2num = {}
        seen = defaultdict(list)
        for i in range(len(nums)):
            index2num[i] = nums[i]
            if seen[nums[i]]:
                for j in seen[nums[i]]:
                    if abs(i-j) <=k:
                        return True        
            seen[nums[i]].append(i)
        return False
