'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-06
    * Time : 2:45 p.m.
    * Question :(https://leetcode.com/problems/reverse-string/)
        Write a function that reverses a string. The input string is given as an array of characters s.

        You must do this by modifying the input array in-place with O(1) extra memory.
    * Example :
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=[x for x in sys.stdin.readline().rstrip('\n').split()]
        i = 0
        j = len(s) - 1
        while (i < j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        print(s)
