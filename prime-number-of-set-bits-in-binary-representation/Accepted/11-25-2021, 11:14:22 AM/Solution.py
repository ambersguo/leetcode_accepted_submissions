// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation

class Solution:
    def isPrime(self, num: int) -> bool:
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            for n in range(2, num):
                if num%n == 0:
                    return False
            return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        setbits = []
        prime_count = 0
        for n in range(left,right+1):
            n_bin = format(n,'b')
            n_bin_str = str(n_bin)
            count = 0
            for s in n_bin_str:
                if s == '1':
                    count += 1
            setbits.append(count)
        for n in setbits:
            if self.isPrime(n):
                prime_count += 1
        return prime_count
