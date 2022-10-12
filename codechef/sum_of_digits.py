'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 1:07 a.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/FLOW006)
        You're given an integer N. Write a program to calculate the sum of all the digits of N.
    * Example :
        Input
        3
        12345
        31203
        2123
        Output
        15
        9
        8
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=sys.stdin.readline().rstrip('\n')
        digits_sum=0
        for i in n:
            digits_sum+=(int(i))
        sys.stdout.write(str(digits_sum)+'\n')