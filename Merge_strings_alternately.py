"""
url_problem = https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

Вам даны две строки word1 и word2. Объедините строки, добавляя буквы в порядке их чередования,начиная со строки
слово1. Если одна из строк длиннее другой, добавьте дополнительные буквы в конец объединенной строки. Возвращаем
объединенную строку.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""


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
