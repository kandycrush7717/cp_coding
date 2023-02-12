'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-12
    * Time : 6:03 p.m.
    * Question :(https://leetcode.com/problems/evaluate-reverse-polish-notation/)
        You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

        Evaluate the expression. Return an integer that represents the value of the expression.

        Note that:

        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.
    * Example :
        Input: tokens = ["2","1","+","3","*"]
        Output: 9
'''
class Solution:
    def add(self,val1,val2):
        return val1+val2
    def sub(self,val1,val2):
        return val1-val2
    def div(self,val1,val2):
        return int(val1/val2)
    def mul(self,val1,val2):
        return val1*val2
    def evalRPN(self, tokens: List[str]) -> int:
        operators={'+':self.add,'-':self.sub,'/':self.div,'*':self.mul}
        stk=[]
        for i in tokens:
            if i in operators:
                val2=stk.pop()
                val1=stk.pop()
                stk.append(operators[i](val1,val2))
            else:
                stk.append(int(i))
        return stk.pop()
