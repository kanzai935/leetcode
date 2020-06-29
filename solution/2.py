# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sumListNodeRevserse(self, li: ListNode) -> int:
        return li.next.next.val * 100 + li.next.val * 10 + li.val

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_l2_sum = self.sumListNodeRevserse(l1) + self.sumListNodeRevserse(l2)

        answer_list = []

        while (l1_l2_sum > 10):
            answer_list.append(l1_l2_sum % 10)
            l1_l2_sum //= 10
            if (l1_l2_sum < 10):
                answer_list.append(l1_l2_sum)

        answer_list_node = []
        for answer in answer_list[::-1]:
            li = ListNode(answer)
