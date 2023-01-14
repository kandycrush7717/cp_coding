'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-14
    * Time : 2:03 p.m.
    * Question :(https://leetcode.com/problems/reverse-linked-list/)
        Given the head of a singly linked list, reverse the list, and return the reversed list.
    * Example :
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]
'''
import sys

class ListNode:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=ListNode(data)
        current=self.head
        if self.head!=None:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
    def printLinkedList(self):
        current=self.head
        while(current!=None):
            print(current.data,end=' ')
            current=current.next
        print()
    def reverseLinkedList(self):
        prev=None
        curr=self.head
        while(curr!=None):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        num_data=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        linkedlist=LinkedList()
        for i in num_data:
            linkedlist.insert(i)
        linkedlist.printLinkedList()
        linkedlist.reverseLinkedList()
        linkedlist.printLinkedList()