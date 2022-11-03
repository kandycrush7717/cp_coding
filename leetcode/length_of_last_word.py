'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-02
    * Time : 8:11 p.m.
    * Question :(https://leetcode.com/problems/length-of-last-word/)
        Given a string s consisting of words and spaces, return the length of the last word in the string.
    * Example :
        Input: s = "Hello World"
        Output: 5
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        ans=len((s.rstrip(' ').split()))[-1]
        sys.stdout.write(str(ans)+'\n')
