'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-20
    * Time : 7:29 p.m.
    * Question :(https://leetcode.com/problems/merge-two-sorted-lists/)
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first
        two lists.
        Return the head of the merged linked list.
    * Example :
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        out = d
        curr1 = list1
        curr2 = list2
        while (curr1 != None and curr2 != None):
            temp = None
            if curr1.val <= curr2.val:
                temp = curr1
                curr1 = curr1.next
                temp.next = None
            else:
                temp = curr2
                curr2 = curr2.next
                temp.next = None
            out.next = temp
            out = out.next
        if curr1 != None:
            out.next = curr1
        elif curr2 != None:
            out.next = curr2
        return d.next
