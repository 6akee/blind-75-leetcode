## Array


### [Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/description/)
    Difficult : Easy

    Given a zero-based permutation nums (0-indexed), build an array ans of the same 
    length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

    Example 1: 
            Input: nums = [0,2,1,5,3,4]
            Output: [0,1,2,4,5,3]
    Example 2: 
            Input: nums = [5,0,1,2,3,4]
            Output: [4,5,0,1,2,3]
    
    class Solution: # O(n)
        def buildArray(self, nums: List[int]) -> List[int]:
            return [nums[nums[i]] for i in range(len(nums))]

### [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/description/)
    Difficult : Easy

    Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    Specifically, ans is the concatenation of two nums arrays.
    Return the array ans.
    
    Example 1: 
            Input: nums = [1,2,1]
            Output: [1,2,1,1,2,1]
    Example 2: 
            Input: nums = [1,3,2,1]
            Output: [1,3,2,1,1,3,2,1]
    
    class Solution: # O(n)
        def getConcatenation(self, nums: List[int]) -> List[int]:
            ans = nums.copy()
            for i in nums:
                ans.append(i)
                
            return ans

### [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/description/)
    Difficult : Easy

    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    Example 1: 
            Input: nums = [1,2,3,1,1,3]
            Output: 4
    Example 2: 
            Input: nums = [1,1,1,1]
            Output: 6
    
    class Solution: # O(n)
        def numIdenticalPairs(self, nums: List[int]) -> int:
            result = {}
            count = 0

            for num in nums:
                count = count + result.get(num, 0)
                result[num] = result.get(num, 0) + 1
            return count

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
    
    class Solution: # O(n)
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            map_result = {}
            for index, value in enumerate(nums):
                diff = target - value
                if diff in map_result:
                    return [map_result[diff], index]
                map_result[index] = value

### [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
    Difficult : Easy

    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1: 
            Input: prices = [7,1,5,3,6,4]
            Output: 5
    Example 2: 
            Input: prices = [7,6,4,3,1]
            Output: 0
    
    class Solution: # O(n)
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
    
    class Solution: # O(n)
        def containsDuplicate(self, nums: List[int]) -> bool:
            set_nums = set()
            for num in nums:
                if num in set_nums:
                    return True
                set_nums.add(num)
            return False
            
