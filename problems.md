## Arrays & Hashing


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

### [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)
    Difficult : Easy

    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1: 
            Input: s = "anagram", t = "nagaram"
            Output: true
    Example 2: 
            Input: nums = s = "rat", t = "cat
            Output: false
    
    class Solution:
        class Solution:
            def isAnagram(self, s: str, t: str) -> bool:
                if len(s) != len(t):
                    return False
                check_s = {}
                check_t = {}
                for word in t:
                    check_t[word] = check_t.get(word, 0) + 1
                for word in s:
                    check_s[word] = check_s.get(word, 0) + 1
                return check_s == check_t


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


### [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)
    Difficult : Medium

    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Example 1: 
            Input: strs = ["eat","tea","tan","ate","nat","bat"]
            Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Example 2: 
            Input: strs = [""]
            Output: [""]
    
    class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            result = {}
            
            for word in strs:
                anagram = "".join(sorted(word))
                if anagram in result.keys():
                    result[anagram].append(word)
                else:
                    result[anagram] = [word]
            return list(result.values())
