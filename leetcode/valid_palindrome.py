'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-05
    * Time : 1:09 p.m.
    * Question :(https://leetcode.com/problems/valid-palindrome/)
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
        all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
        letters and numbers.
        Given a string s, return true if it is a palindrome, or false otherwise.
    * Example :
        Input: s = "A man, a plan, a canal: Panama"
        Output: true
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        k = ''
        for i in s:
            if i.isdigit() or i.isalpha():
                k += (i.lower())
        flag=(k == k[::-1])
        sys.stdout.write(str(flag)+'\n')