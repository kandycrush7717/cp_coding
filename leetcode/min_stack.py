'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-12
    * Time : 5:25 p.m.
    * Question :(https://leetcode.com/problems/min-stack/)
        Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

        Implement the MinStack class:

        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.
        You must implement a solution with O(1) time complexity for each function.
    * Example :
        Input
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

        Output
        [null,null,null,null,-3,null,0,-2]
'''
class MinStack:
    def __init__(self):
        self.vals=[]
        self.min_vals=[]
    def push(self, val: int) -> None:
        self.vals.append(val)
        self.min_vals.append(min(val,self.min_vals[-1] if len(self.min_vals)>0 else val))
    def pop(self) -> None:
        self.vals.pop()
        self.min_vals.pop()
    def top(self) -> int:
        return self.vals[-1]
    def getMin(self) -> int:
        return self.min_vals[-1]