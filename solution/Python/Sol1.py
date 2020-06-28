from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answers: Dict[int, int] = {}
        i: int
        for i, num in enumerate(nums):
            x = target - num
            if x in answers:
                return [answers[x], i]
            answers[num] = i


nums = [2, 7, 11, 15]
target = 9

print("Input nums:" + "".join(str(nums)))
print("Input target:" + str(target))
print("Output:" + "".join(str(Solution().twoSum(nums, target))))
