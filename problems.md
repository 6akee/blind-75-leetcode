## Array / String


### [Two Sum](https://leetcode.com/problems/two-sum/description/)
    Difficult : Easy

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.



    Example 1: 
            Input: nums = [2,7,11,15], target = 9
            Output: [0,1]
    Example 2: 
            Input: nums = [3,2,4], target = 6
            Output: [1,2]
    
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            mapping = {}

            for index, val in enumerate(nums):
                diff = target - val
                if diff in mapping:
                    return [mapping[diff], index]
                else:
                    mapping[val] = index

### [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/description/)
    Difficult : Easy

    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].



    Example 1: 
            Input: nums = [2,5,1,3,4,7], n = 3
            Output: [2,3,5,4,1,7]
    Example 2: 
            Input: nums = [1,2,3,4,4,3,2,1], n = 4
            Output: [1,4,2,3,3,2,4,1]
    
    class Solution:
        def shuffle(self, nums: List[int], n: int) -> List[int]:
            ans = []
            for i in range(n):
                ans.append(nums[i])
                ans.append(nums[i+n])
            return ans
