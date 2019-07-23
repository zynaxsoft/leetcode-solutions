""" https://leetcode.com/problems/add-two-numbers/"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import itertools

def list_generator(node):
    yield node
    cur_node = node
    while cur_node.next:
        cur_node = cur_node.next
        yield cur_node
    raise StopIteration
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        cur_node = None
        iterable_l1 = list(list_generator(l1))
        iterable_l2 = list(list_generator(l2))
        l1_length = len(iterable_l1)
        l2_length = len(iterable_l2)
        filler = ListNode(0)
        
        for n1, n2 in itertools.zip_longest(iterable_l1, iterable_l2, fillvalue=filler):
            summation = n1.val + n2.val + carry
            carry = 0
            if summation > 9:
                carry = 1
                summation -= 10
            if l1_length >= l2_length:
                n1.val = summation
            else:
                n2.val = summation
        
        if l1_length >= l2_length:
            if carry > 0:
                n1.next = ListNode(1)
            return l1
        else:
            if carry > 0:
                n2.next = ListNode(1)
            return l2
