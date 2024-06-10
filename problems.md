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
    
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            map_result = {}
            for index, value in enumerate(nums):
                diff = target - value
                if diff in map_result:
                    return [map_result[diff], index]
                map_result[index] = value

