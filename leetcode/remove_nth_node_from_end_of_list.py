'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-08
    * Time : 12:35 p.m.
    * Question :(https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
    * Example :
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]
'''

def removeNthFromEnd(head, n) :
    l = 0
    curr = head
    while curr != None:
        l += 1
        curr = curr.next
    pff = l - n
    curr = head
    curr_pos = 0
    prev = head
    while curr_pos != pff:
        curr_pos += 1
        prev = curr
        curr = curr.next
    if curr_pos == 0:
        head = curr.next
    else:
        prev.next = curr.next
    return head
