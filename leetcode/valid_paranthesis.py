'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-11
    * Time : 12:08 p.m.
    * Question :(https://leetcode.com/problems/valid-parentheses/)
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string
        is valid
        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.
    * Example :
        Input: s = "()[]{}"
        Output: true
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        close_dict = {')': '(', ']': '[', '}': '{'}
        open_set = set(['(', '{', '['])
        stk = []
        flag=True
        for i in s:
            if i in open_set:
                stk.append(i)
            else:
                if len(stk) > 0:
                    if stk[-1] == close_dict[i]:
                        stk.pop(-1)
                    else:
                        flag=False
                else:
                    flag=False
        flag=len(s)==0
        sys.stdout.write(str(flag)+'\n')