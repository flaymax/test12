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


print(Solution().twoSum([int(input()) for i in range(3)], int(input())))
print(np.exp(np.pi))



