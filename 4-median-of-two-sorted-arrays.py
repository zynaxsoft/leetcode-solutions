""" https://leetcode.com/problems/median-of-two-sorted-arrays/"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l3 = nums1 + nums2
        l3.sort()
        if len(l3) % 2 == 0:
            index = int(len(l3)/2)-1
            return (l3[index] + l3[index+1])/2
        return l3[int(len(l3)/2)]
