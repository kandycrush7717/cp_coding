'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 1:11 a.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/FLOW007)
        Given an Integer N, write a program to reverse it.
    * Example :
        Input:
        4
        12345
        31203
        2123
        2300
        Output:
        54321
        30213
        3212
        32
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=sys.stdin.readline().rstrip('\n')
        n=n.strip('0')
        reverse=n[::-1]
        sys.stdout.write(reverse+'\n')