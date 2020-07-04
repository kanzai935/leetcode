from typing import List


class Solution:
    def longest_palindrome(self, s: str) -> str:

        strings: List[str] = list(s)
        strings_length: int = len(strings)

        longest_str: str = ""
        longest_length: int = 0
        for i in range(strings_length):
            for j in range(strings_length):
                if i > j:
                    continue

                strings_slice: List[str] = strings[i:j + 1]
                strings_slice_length: int = len(strings_slice)

                if strings_slice == list(reversed(strings_slice)) and strings_slice_length > longest_length:
                    longest_length = strings_slice_length
                    longest_str = "".join(strings_slice)
                    print(longest_length)
        return longest_str
