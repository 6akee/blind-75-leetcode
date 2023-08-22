url_problem = ("https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2"
               "&envId=leetcode-75")


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
