url_problem = ("https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan"
               "-v2&envId=leetcode-75")


class Solution:  # O(n)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res_list = []

        for can in candies:
            count_candies = can + extraCandies
            res_list.append(count_candies >= max_candies)

        return res_list

