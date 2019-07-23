""" https://leetcode.com/problems/reverse-integer/ """
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x).split('-')
        i = int(s[-1][::-1])
        if i > 2**31-1 or i < -1*2**31:
            return 0
        if len(s) > 1:
            return -1*i
        return i
