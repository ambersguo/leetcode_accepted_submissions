// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_uniq = list(set(nums))
        numsdict = {}
        dis = []
        for n in nums_uniq:
            numsdict[n] = n
        for i in range(1,len(nums)+1):
            if i in numsdict:
                next
            else:
                dis.append(i)
        return dis
