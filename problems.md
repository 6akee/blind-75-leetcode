## Easy


### [Two Sum](https://leetcode.com/problems/two-sum/description/)
    Difficult : Easy

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Example 1: 
            Input: nums = [2,7,11,15], target = 9
            Output: [0, 1]
    Example 2: 
            Input: nums = [3,2,4], target = 6
            Output: [1, 2]
    
    class Solution: # Time and Space O(n)
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            map_result = {}  # Создаем словарь для хранения значений и их индексов
            for index, value in enumerate(nums):
                diff = target - value  # Вычисляем разницу между целевым значением и текущим элементом
                if diff in map_result:
                    return [map_result[diff], index]  # Если разница уже есть в словаре, возвращаем индексы
                map_result[value] = index  # Сохраняем текущий элемент и его индекс в словарь
            return []  # Возвращаем пустой список, если не найдено решение (этот случай не предусмотрен по условию задачи)



## [Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/)
    Difficult : Easy

    Given a roman numeral, convert it to an integer.

    Example 1: 
            Input: s = "III"
            Output: 3
    Example 2: 
            Input: s = "LVIII"
            Output: 58
    
    class Solution: # Time O(n) Space O(1)
        def romanToInt(self, s: str) -> int:
            # Словарь с римскими цифрами и их значениями
            roman = {
                'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 
                'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 
                'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
            }
            
            i = 0  # Индекс для обхода строки
            num = 0  # Итоговое число
            
            # Пока не пройдем всю строку
            while i < len(s):
                # Проверяем, есть ли комбинация из двух символов в словаре
                if i + 1 < len(s) and s[i:i+2] in roman:
                    num += roman[s[i:i+2]]  # Добавляем значение этой комбинации
                    i += 2  # Пропускаем два символа
                else:
                    num += roman[s[i]]  # Добавляем значение одного символа
                    i += 1  # Пропускаем один символ
            return num

## [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/)
    Difficult : Easy

    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example 1: 
            Input: strs = ["flower","flow","flight"]
            Output: "fl"
    Example 2: 
            Input: strs = ["dog","racecar","car"]
            Output: ""
    
    class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: Time O(n*m) Space O(1)
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if (i == len(word)) or (word[i] != base[i]):
                    return base[0:i]

        return base
