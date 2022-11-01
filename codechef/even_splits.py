'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-31
    * Time : 10:35 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/EVENSPLIT)
        You are given a binary string S of length N. You can perform the following operation on it:
            Pick any non-empty even-length subsequence of the string.
            Suppose the subsequence has length 2k. Then, move the first k characters to the beginning of S and the
            other k to the end of S (without changing their order).
        What is the lexicographically smallest string that can be obtained after performing this operation
        several (possibly, zero) times?
    * Example :
        Input :
            4
            2
            10
            4
            1001
            5
            11111
            7
            0010100
        Output :
            10
            0011
            11111
            0000011
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        s=list(sys.stdin.readline().rstrip('\n'))
        if len(s)>2:
            s.sort()
        ans=''
        for i in s:
            ans+=i
        sys.stdout.write(ans+'\n')
