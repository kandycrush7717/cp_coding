'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-02
    * Time : 7:56 p.m.
    * Question :(https://leetcode.com/problems/is-subsequence/)
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    * Example :
        Input: s = "abc", t = "ahbgdc"
        Output: true
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        k=sys.stdin.readline().rstrip('\n')
        i=j=0
        s_len=len(s)
        k_len=len(k)
        while(i<s_len and j<k_len):
            if s[i]==k[j]:
                i+=1
            j+=1
        flag=(i==s_len)
        sys.stdout.write(str(flag)+'\n')