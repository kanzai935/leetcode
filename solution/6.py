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
    ----------------
    P  I     N
    A L S   I G
    YA   H R
    P     I
    ----------------
    PI N
    ALSIG
    YAHR
    P I
    ----------------
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    ----------------
    P  A   H   N
    A P L S I I G
    Y    I   R
    ----------------
    PA H N
    APLSIIG
    Y I R
    ----------------
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    """

    @staticmethod
    def convert(s: str, num_rows: int) -> str:

        s_list = []
        s_length = len(s)
        num_element = 0  # 文字列を入れる箱の数

        for i in range(s_length):

            if i % num_rows != 0 and num_element * num_rows <= s_length:
                print("A")
                continue

            # 文字列を入れる箱を用意する
            s_list.append([])

            # 1番目〜num_rows番目までの文字列を格納する
            if i == 0:
                print("B")
                s_list[num_element].append(s[i:i + num_rows])
                num_element += 1
                continue

            # 文字列を入れる箱の数が偶数かつ、格納している文字列の総数が文字列の長さより短いとき
            if num_element % 2 == 0 and num_element * num_rows <= s_length:
                print("C")
                s_list[num_element].append(str(0) + s[i - num_element + 1:i + num_rows - num_element])

            # 文字列を入れる箱の数が偶数かつ、格納している文字列の総数が文字列の長さより長いとき
            elif num_element % 2 == 0 and num_element * num_rows > s_length:
                print("D")
                s_list[num_element].append(str(0))
                s_list[num_element][0] += s[i:s_length]
                for j in range(num_rows - len(s[i:s_length]) - 1):
                    s_list[num_element][0] += str(0)
                break

            # 文字列を入れる箱の数が奇数かつ、格納している文字列の総数が文字列の長さより短いとき
            elif num_element % 2 != 0 and num_element * num_rows <= s_length:
                print("E")
                s_list[num_element].append(s[i - num_element + 1:i + num_rows - num_element][::-1] + str(0))

            # 文字列を入れる箱の数が奇数かつ、格納している文字列の総数が文字列の長さより長いとき
            elif num_element % 2 != 0 and num_element * num_rows > s_length:
                print("F")
                for j in range(num_rows - len(s[i:s_length][::-1]) - 1):
                    if j == 0:
                        s_list[num_element].append(str(0))
                    else:
                        s_list[num_element][0] += str(0)
                s_list[num_element][0] += s[i:s_length][::-1] + str(0)
                break

            num_element += 1

        converted_s = ""

        for i in range(num_rows):
            for j in range(len(s_list)):
                if list(s_list[j][0])[i] != str(0):
                    converted_s += s_list[j][0][i]

        print(s_list)
        print(s)
        print(len(s))
        print(converted_s)
        print(len(converted_s))

        return converted_s

Solution.convert("PAYPALISHIRING",3)
