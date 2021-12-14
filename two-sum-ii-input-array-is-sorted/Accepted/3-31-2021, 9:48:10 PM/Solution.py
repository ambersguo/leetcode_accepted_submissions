// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers1 = numbers[:]
        for i in range(0,len(numbers)):
            minus = target - numbers[i]
            if minus in numbers[i+1:]:
                index1 = i
                if minus == numbers[i]:
                    del numbers1[i]
                    index2 = numbers1.index(minus)+1
                else:
                    index2 = numbers.index(minus)
                if index1 == index2:
                    i += 1
                else:
                    break
            else:
                i += 1
        answer = [index1+1, index2+1]
        answer.sort()
        return answer
        