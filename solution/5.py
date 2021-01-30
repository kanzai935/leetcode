from typing import List


class Solution:
    """
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    """
    @staticmethod
    def find_longest_palindrome(s: str) -> str:

        strings_list: List[str] = list(s)
        strings_list_length: int = len(strings_list)

        longest_str: str = ""
        longest_str_length: int = 0
        for i in range(strings_list_length):
            for j in range(strings_list_length):
                if i > j:
                    continue

                strings_list_slice: List[str] = strings_list[i:j + 1]
                strings_list_slice_length: int = len(strings_list_slice)

                if strings_list_slice == list(reversed(strings_list_slice)) and strings_list_slice_length > longest_str_length:
                    longest_str_length = strings_list_slice_length
                    longest_str = "".join(strings_list_slice)
        return longest_str
