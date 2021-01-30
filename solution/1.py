from typing import List, Dict


class Solution:
    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    @staticmethod
    def sum_two(nums: List[int], target: int) -> List[int]:

        answers_dict: Dict[int, int] = {}
        for i, num in enumerate(nums):
            x: int = target - num
            if x in answers_dict:
                return [answers_dict[x], i]
            answers_dict[num] = i
        return answers_dict
