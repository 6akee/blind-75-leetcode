"""
url_problem = https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

Для двух строк s и t мы говорим "t делит s" тогда и только тогда, когда s = t + ... + t
(т.е. t конкатенируется с самим собой один или несколько раз).
Если даны две строки str1 и str2, верните наибольшую строку x такую, что x делит и str1, и str2

Пример 1:
Вход: str1 = "ABCABC", str2 = "ABC"
Выходные данные: "ABC"

Пример 2:
Вход: str1 = "ABABAB", str2 = "ABAB"
Выходные данные: "AB"

Пример 3:
Вход: str1 = "LEET", str2 = "CODE"
Выходные данные: ""
"""


class Solution:  # O(n)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):  # Euclidean algorithms
            if a == 0:
                return b

            return gcd(b % a, a)

        diff = gcd(len(str1), len(str2))
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:diff]
