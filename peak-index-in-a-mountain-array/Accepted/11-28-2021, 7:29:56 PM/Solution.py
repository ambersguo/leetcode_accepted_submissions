// https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        index2num = {}
        for i in range(len(arr)):
            index2num[i] = arr[i]
        key_max = max(index2num, key = index2num.get)
        return key_max
