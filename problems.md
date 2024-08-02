## Array


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



### [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
    Difficult : Easy

    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    
    Example 2: 
            Input: prices = [7,6,4,3,1]
            Output: 0
            Explanation: In this case, no transactions are done and the max profit = 0.
    
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            profit = 0
            buy = prices[0]
    
            for sell in prices[1:]:
                if sell > buy:
                   profit = max(profit, sell - buy)
                else:
                    buy = sell
    
            return profit


### [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)
    Difficult : Easy

    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

    Example 1:
        Input: nums = [1,2,3,1]
        Output: true
    
    Example 2:
        Input: nums = [1,2,3,4]
        Output: false
    
    Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
    
    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            uniq_set = set()
    
            for num in nums:
                if num in uniq_set:
                    return True
                uniq_set.add(num)
            return False
