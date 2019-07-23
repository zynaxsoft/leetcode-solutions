""" https://leetcode.com/problems/two-sum/ """
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference not in seen:
                seen[number] = index
            else:
                return [index, seen[difference]]
