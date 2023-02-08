'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-08
    * Time : 11:57 a.m.
    * Question :(https://leetcode.com/problems/reorder-list/)
        You are given the head of a singly linked-list. The list can be represented as:
        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    * Example :
        Input: head = [1,2,3,4]
        Output: [1,4,2,3]

'''
def reorder(head):
    s = head
    f = head.next
    while f != None and f.next != None:
        s = s.next
        f = f.next.next
    sec = s.next
    s.next = None
    prev = None
    while sec != None:
        temp = sec.next
        sec.next = prev
        prev = sec
        sec = temp
    last = prev
    first = head
    while last != None:
        ftemp = first.next
        ltemp = last.next
        first.next = last
        last.next = ftemp
        first = ftemp
        last = ltemp