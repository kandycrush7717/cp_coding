'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-02
    * Time : 6:20 p.m.
    * Question :(https://leetcode.com/problems/valid-anagram/)
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
        the original letters exactly once.
    * Example :
        Input: s = "anagram", t = "nagaram"
        Output: true
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        k=sys.stdin.readline().rstrip('\n')
        flag=sorted(s)==sorted(k)
        sys.stdout.write(str(flag)+'\n')
