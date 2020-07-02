from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        length: int = len(nums1)
        if length % 2 == 0:
            i_1 = length / 2 - 1
            i = length / 2
            num = float((nums1[int(i_1)] + nums1[int(i)]) / 2)
        else:
            i = length // 2
            num = float(nums1[i])
        return num
