'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-11
    * Time : 1:15 p.m.
    * Question :(https://leetcode.com/problems/number-of-1-bits/)
        Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as
        the Hamming weight).
    * Example :
        Input: n = 11111111111111111111111111111101
        Output: 31
        Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        count = 0
        while (n != 0):
            if n & 1 != 0:
                count += 1
            n >>= 1
        sys.stdout.write(str(count)+'\n')
'''
        Other Approach
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        count = 0
        while (n != 0):
            n=n&n-1
            count+=1
        sys.stdout.write(str(count)+'\n')
'''