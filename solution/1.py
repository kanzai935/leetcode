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