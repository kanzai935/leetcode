from typing import List, Dict


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:

        answers: Dict[int, int] = {}
        for i, num in enumerate(nums):
            x: int = target - num
            if x in answers:
                return [answers[x], i]
            answers[num] = i
        return answers
