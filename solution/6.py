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
            if i % num_rows != 0 and count * num_rows < s_length:
                continue

            s_list.append([])

            if i == 0:
                s_list[count].append(s[i:i + num_rows - count])
                count += 1
                continue

            if count % 2 == 0 and count * num_rows < s_length:
                s_list[count].append(str(0) + s[i - count + 1:i + num_rows - count])

            elif count % 2 == 0 and count * num_rows > s_length:
                s_list[count].append(str(0))
                s_list[count][0] += s[i:s_length]
                for j in range(num_rows - len(s[i:s_length]) - 1):
                    s_list[count][0] += str(0)
                    break

            elif count % 2 != 0 and count * num_rows < s_length:
                s_list[count].append(s[i - count + 1:i + num_rows - count][::-1] + str(0))

            elif count % 2 != 0 and count * num_rows > s_length:
                for j in range(num_rows - len(s[i:s_length][::-1]) - 1):
                    if j == 0:
                        s_list[count].append(str(0))
                    else:
                        s_list[count][0] += str(0)
                s_list[count][0] += s[i:s_length][::-1] + str(0)
                break

            count += 1

        converted_s = ""

        for i in range(num_rows):
            for j in range(len(s_list)):
                if list(s_list[j][0])[i] != str(0):
                    converted_s += s_list[j][0][i]

        print(converted_s)
        print(len(converted_s))

        return converted_s

Solution.convert("FUYUHASAMUIMAINICHINEMUI", 5)
