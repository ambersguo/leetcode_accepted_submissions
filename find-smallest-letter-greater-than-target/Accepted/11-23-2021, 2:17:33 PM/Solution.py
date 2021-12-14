// https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters_set = set(letters)
        letters = list(letters_set)
        letters.sort()
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        elif target == letters[0]:
            return letters[1]
        else:
            start = 0
            end = len(letters)-1
            mid = int(len(letters)/2)
            while end - start > 1:
                mid = int((start+end)/2)
                if target == letters[mid]:
                    return letters[mid+1]
                elif target > letters[mid]:
                    start = mid
                else:
                    end = mid
            return letters[end]
