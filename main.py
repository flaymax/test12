import numpy as np

class Solution:
    def twoSum(self, nums, target):
        s = -1
        k = 0
        answer = []
        for i in nums:
            s += 1
            k = 0
            if len(answer) == 0:
                for j in nums:
                    if target == i + j and s != k:
                        answer.append(s)
                        answer.append(k)
                        return answer
                    else:
                        k += 1


class sumi:
    def factorial1(self, n):
        return n * self.factorial1(n - 1) if n > 1 else 1
    def sum_factorial(self, n):
        summ=0
        for i in range(n+1):
            summ += self.factorial1(i)
        return summ

print(Solution().twoSum([int(input()) for i in range(3)], int(input())))
print(sumi().sum_factorial(9))
print('успех')





