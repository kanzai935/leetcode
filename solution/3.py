from typing import List


class Solution:
    """
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    """
    @staticmethod
    def find_length_of_longest_substring(s: str) -> int:

        substrings_list: List[str] = []
        length_of_longest: int = 0
        for string in list(s):
            if string in substrings_list: substrings_list = substrings_list[substrings_list.index(string) + 1:]
            substrings_list.append(string)
            if len(substrings_list) > length_of_longest: length_of_longest = len(substrings_list)
        return length_of_longest
