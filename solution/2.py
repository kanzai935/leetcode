# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def sum_reverse_order_list_node(li: ListNode) -> int:

        nums: List[int] = []
        while li.next:
            nums.append(li.val)
            li = li.next
        nums.append(li.val)
        return sum([num * 10 ** i for i, num in enumerate(nums)])

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        sum_l1_l2: int = self.sum_reverse_order_list_node(l1) + self.sum_reverse_order_list_node(l2)

        sum_l1_l2_nums: List[int] = []
        while sum_l1_l2 >= 10:
            sum_l1_l2_nums.append(sum_l1_l2 % 10)
            sum_l1_l2 //= 10
        sum_l1_l2_nums.append(sum_l1_l2)

        node: ListNode = None
        nodes: List[ListNode] = []
        for i, num in enumerate(sum_l1_l2_nums[::-1]):
            node = ListNode(num, None) if i == 0 else ListNode(num, nodes[i - 1])
            nodes.append(node)
        return node
