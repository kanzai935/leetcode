from typing import List


class Solution:
    """
    F   M       C
    U  A U     I H     I
    Y S   I   N   I   U
    UA     M I     N M
    H       A       E
    ----------------
    Input: s = "FUYUHASAMUIMAINICHINEMUI", numRows = 5
    Output: "FMCUAUIHIYSINIUUAMINMHAE"
    """

    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        string_length = len(s)
        s_1 = s[0:5]
        s_2 = s[5:9][::-1]
        s_3 = s[9:13]
        s_4 = s[13:17][::-1]
        s_5 = s[17:21]
        s_6 = s[21:24][::-1]
        print(s_1)
        print(s_2)
        print(s_3)
        print(s_4)
        print(s_5)
        print(s_6)

Solution.convert("FUYUHASAMUIMAINICHINEMUI", 5)
