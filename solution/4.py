from typing import List


class Solution:
    """
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
    """
    @staticmethod
    def find_median_sorted_arrays(nums1_list: List[int], nums2_list: List[int]) -> float:

        nums1_list.extend(nums2_list)
        nums1_list.sort()

        length: int = len(nums1_list)
        if length % 2 == 0:
            i_1 = length / 2 - 1
            i = length / 2
            num = float((nums1_list[int(i_1)] + nums1_list[int(i)]) / 2)
        else:
            i = length // 2
            num = float(nums1_list[i])
        return num
