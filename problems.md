## Array


### [Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/description/)
    Difficult : Easy

    Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.



    Example 1: 
            Input: nums = [0,2,1,5,3,4]
            Output: [0,1,2,4,5,3]
    Example 2: 
            Input: nums = [5,0,1,2,3,4]
            Output: [4,5,0,1,2,3]
    
    class Solution:
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
    
    class Solution:
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
    
    class Solution:
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
    
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            map_result = {}
            for index, value in enumerate(nums):
                diff = target - value
                if diff in map_result:
                    return [map_result[diff], index]
                map_result[index] = value