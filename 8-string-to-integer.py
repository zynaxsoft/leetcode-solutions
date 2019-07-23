""" https://leetcode.com/problems/string-to-integer-atoi/"""
import re

class Solution:
    def myAtoi(self, in_str: str) -> int:
        p = re.compile("(\s*)([-,+]?\d+)")
        p = p.match(in_str)
        if p is None:
            return 0
        value = int(p.group(2))
        if value > 2**31 - 1:
            return 2**31 -1
        elif value < -1 * 2**31:
            return -1 * 2**31
        return value
