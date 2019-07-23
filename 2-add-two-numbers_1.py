""" https://leetcode.com/problems/add-two-numbers"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import itertools

def list_generator(node):
    yield node.val
    cur_node = node
    while cur_node.next:
        cur_node = cur_node.next
        yield cur_node.val
    raise StopIteration
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        cur_node = None
        for v1, v2 in itertools.zip_longest(list_generator(l1), list_generator(l2), fillvalue=0):
            carry, v3 = divmod(v1 + v2 + carry, 10)
            prev_node = cur_node
            cur_node = ListNode(v3)
            if prev_node is not None:
                prev_node.next = cur_node
            else:
                head_node = cur_node
        if carry > 0:
            cur_node.next = ListNode(1)
        return head_node
