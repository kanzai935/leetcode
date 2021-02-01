from typing import List


class Solution:
    """
    F   M       C
    U  A U     I H     I
    Y S   I   N   I   U
    UA     M I     N M
    H       A       E
    ----------------
    FM C
    UAUIHI
    YSINIU
    UAMINM
    H A E
    ----------------
    Input: s = "FUYUHASAMUIMAINICHINEMUI", numRows = 5
    Output: "FMCUAUIHIYSINIUUAMINMHAE"
    """

    @staticmethod
    def convert(s: str, num_rows: int) -> str:

        s_list = []
        s_length = len(s)
        count = 0

        for i in range(s_length):
            if i % 5 != 0 and count * 5 < s_length:
                continue

            s_list.append([])

            if i == 0:
                s_list[count].append(s[i:i + num_rows - count])
                count += 1
                continue

            if count % 2 == 0 and count * 5 < s_length:
                s_list[count].append(s[i - count + 1:i + num_rows - count])

            elif count % 2 == 0 and count * 5 > s_length:
                s_list[count].append(s[i:s_length])
                break

            elif count % 2 != 0 and count * 5 < s_length:
                s_list[count].append(s[i - count + 1:i + num_rows - count][::-1])

            elif count % 2 != 0 and count * 5 > s_length:
                s_list[count].append(s[i:s_length][::-1])
                break

            count += 1

        print(s_list)

        s_1 = s[0:5]
        s_2 = s[5:10-1][::-1]
        s_3 = s[10-1:15-2]
        s_4 = s[15-2:20-3][::-1]
        s_5 = s[20-3:25-4]
        s_6 = s[25-4:24][::-1]

Solution.convert("FUYUHASAMUIMAINICHINEMUI", 5)
