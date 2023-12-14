## Array / String


### [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75)
    Difficult : Easy

    You are given two strings word1 and word2. 
    Merge the strings by adding letters in alternating order, starting with word1. 
    If a string is longer than the other, append the additional letters onto the end of the merged string.
    Return the merged string.

    Example 1: 
            Input: word1 = "abc", word2 = "pqr"
            Output: "apbqcr"
    Example 2: 
            Input: word1 = "abcd", word2 = "pq"
            Output: "apbqcd"
    
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
### [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75)
    Difficult : Easy

    For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
    (i.e., t is concatenated with itself one or more times).
    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

    Example 1: 
            Input: str1 = "ABCABC", str2 = "ABC"
            Output: "ABC"
    Example 2: 
            Input: str1 = "ABABAB", str2 = "ABAB"
            Output: "AB"
    
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
### [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75)
    Difficult : Easy

    We have n children with candies. Each child has a certain number of candies, represented as an array of integers candies[i], 
    where i is the number of the child. We also have additional candies, labeled extraCandies.
    We need to return a Boolean array result of length n, where result[i] is True if, 
    after we give all children of the i-th child all extra candies, it has the highest number of candies among all children. Otherwise, result[i] is False.
    Note that several children can have the same maximum number of candies.

    Example 1: 
            Input: candies = [2,3,5,1,3], extraCandies = 3
            Output: [true,true,true,false,true]
    Example 2: 
            Input: candies = [4,2,1,1,2], extraCandies = 1
            Output: [true,false,false,false,false] 
    
    class Solution:  # O(n)
        def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
            max_candies = max(candies)
            res_list = []
    
            for can in candies:
                count_candies = can + extraCandies
                res_list.append(count_candies >= max_candies)
    
            return res_list
### [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75)
    Difficult : Easy

    Given a string s, reverse only all the vowels in the string and return it.
    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
    
    Example 1: 
            Input: s = "hello"
            Output: "holle"
    Example 2: 
            Input: s = "leetcode"
            Output: "leotcede" 
    
    class Solution:  # O(n)
        def reverseVowels(self, s: str) -> str:
            vowels = "aeiouAEIOU"
            s = list(s)
            left, right = 0, len(s) - 1

            while left < right:
                while left < right and s[left] not in vowels:
                    left += 1
                while left < right and s[right] not in vowels:
                    right -= 1
    
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
    
            return ''.join(s)
### [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75)
    Difficult : Easy

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
    return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule 
    and false otherwise.

    Example 1: 
            Input: flowerbed = [1,0,0,0,1], n = 1
            Output: true
    Example 2: 
            Input: flowerbed = [1,0,0,0,1], n = 1
            Output: false 
    
    class Solution:  # O(n)
        def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
            count = 0
            for i in range(len(flowerbed)):
                if flowerbed[i] == 0:
                    empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                    empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                    if empty_left_plot and empty_right_lot:
                        flowerbed[i] = 1 # add flower
                        count += 1
            return count >= n
### [Revers Vowels of a string](https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75)
    Difficult : Medium

    Given an input string s, reverse the order of the words.
    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
    Return a string of the words in reverse order concatenated by a single space.

    Example 1: 
            Input: s = "the sky is blue"
            Output: "blue is sky the"
    Example 2: 
            Input: s = "  hello world  "
            Output: world hello 
    
    class Solution: # O(n)
        def reverseWords(self, s: str) -> str:
            s = s.strip()
            s = s.split()
            result = [s[txt] for txt in range(len(s) - 1, - 1, - 1)]
    
            return ' '.join(result)
