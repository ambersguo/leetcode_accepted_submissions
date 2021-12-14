// https://leetcode.com/problems/lemonade-change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        else:
            five_usd = 1
            ten_usd = 0
            twenty_usd = 0
            for i in range(1,len(bills)):
                if bills[i] == 5:
                    five_usd += 1
                else:   
                    if bills[i] == 10:
                        if five_usd == 0:
                            return False
                        else:
                            ten_usd += 1
                            five_usd -= 1
                    else:
                        if ten_usd > 0:
                            ten_usd -= 1
                            if five_usd == 0:
                                return False
                            else:
                                five_usd -= 1
                        else:
                            if five_usd < 3:
                                return False
                            else:
                                five_usd -= 3
                                twenty_usd += 1
            return True
