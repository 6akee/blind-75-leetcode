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


### [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
    Difficult : Medium

    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.

    Example 1: 
            Input: nums = [1,1,1,2,2,3], k = 2
            Output: [1,2]
    Example 2: 
            Input: nums = [1], k = 1
            Output: [1]
    
    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            if len(nums) == k:
                return nums
    
            counter = Counter(nums)
    
            result = [item[0] for item in counter.most_common(k)]
    
            return result


### [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)
    Difficult : Medium

    Given an integer array nums, return an array answer such that answer[i] is equal to the 
    product of all the elements of nums except nums[i].

    Example 1: 
            Input: nums = [1,2,3,4]
            Output: [24,12,8,6]
    Example 2: 
            Input: nums = [-1,1,0,-3,3]
            Output: [0,0,9,0,0]
    
    class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            length = len(nums)
            products = [1] * length
            for i in range(1, length):
                products[i] = products[i-1] * nums[i - 1]
            right = nums[-1]
            for i in range(length-2, -1, -1):
                products[i] *= right
                right *= nums[i] 
            return products



### [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)
    Difficult : Medium

    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
    need to be validated according to the following rules:
    1.Each row must contain the digits 1-9 without repetition.
    2.Each column must contain the digits 1-9 without repetition.
    3.Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Example 1: 
            Input: board = 
                        [["5","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]
            Output: true
    Example 2: 
            Input: board = 
                        [["8","3",".",".","7",".",".",".","."]
                        ,["6",".",".","1","9","5",".",".","."]
                        ,[".","9","8",".",".",".",".","6","."]
                        ,["8",".",".",".","6",".",".",".","3"]
                        ,["4",".",".","8",".","3",".",".","1"]
                        ,["7",".",".",".","2",".",".",".","6"]
                        ,[".","6",".",".",".",".","2","8","."]
                        ,[".",".",".","4","1","9",".",".","5"]
                        ,[".",".",".",".","8",".",".","7","9"]]
            Output: false
    
    class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            cols = collections.defaultdict(set)
            rows = collections.defaultdict(set)
            squares = collections.defaultdict(set)
    
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        continue
                    if (board[r][c] in rows[r] or
                            board[r][c] in cols[c] or
                            board[r][c] in squares[(r // 3, c // 3)]):
                        return False
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])
            return True



### [Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)
    Difficult : Easy

    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.

    Example 1: 
            Input: nums = [1,3,5,6], target = 5
            Output: 2
    Example 2: 
            Input: nums = [1,3,5,6], target = 2
            Output: 1
    
    class Solution:
        def searchInsert(self, nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return left


### [Plus One](https://leetcode.com/problems/plus-one/description/)
    Difficult : Easy

    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. 
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    Example 1: 
            Input: nums = [1,2,3]
            Output: [1,2,4]
    Example 2: 
            Input: nums = [9, 9]
            Output: [1, 0, 0]
    
    class Solution:
        def plusOne(self, digits: List[int]) -> List[int]:
            if len(digits) == 1 and digits[0] == 9:
                return [1, 0]

            int_to_str = ""
            for digit in digits:
                int_to_str += str(digit)
            int_to_str = int(int_to_str) + 1
            
            return [int(num) for num in str(int_to_str)]