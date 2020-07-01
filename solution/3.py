from typing import List


class Solution:
    def length_of_longest_substring(self, s: str) -> int:

        substrings: List[str] = []
        longest: int = 0
        for string in list(s):
            if string in substrings:
                substrings = substrings[substrings.index(string) + 1:]
            substrings.append(string)
            if len(substrings) > longest:
                longest = len(substrings)

        return longest
