url_problem = ("https://leetcode.com/problems/merge-strings-"
               "alternately/?envType=study-plan-v2&envId=leetcode-75")


class Solution:  # O(n + m)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1 = len(word1)
        len_w2 = len(word2)
        max_l = max(len(word1), len(word2))
        l = r = 0
        result = ''
        while max_l != 0:
            if len_w1 == 0:
                result += word2[r]
                r += 1
                max_l -= 1
            elif len_w2 == 0:
                result += word1[l]
                l += 1
                max_l -= 1
            else:
                result += word1[l]
                len_w1 -= 1
                result += word2[r]
                len_w2 -= 1
                max_l -= 1
                l += 1
                r += 1
        return result
