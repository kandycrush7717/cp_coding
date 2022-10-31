'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-31
    * Time : 5:06 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/MAXTHEMIN)
        JJ has an array A of size N. He can perform the following operations on the array at most K times:

        Set A_i := A_{i + 1} where 1≤i≤N−1
        Set A_i := A_{i - 1} where 2≤i≤N
        He wants to maximize the value of the minimum element of the array A. Formally, he wants to maximize the value
        of min A_i 1≤i≤N
        Can you help him do so?
    * Example :
        Input :
            4
            5 4
            5 4 3 2 1
            6 1
            8 2 3 9 6 10
            5 2
            4 3 4 3 5
            5 1000
            4 3 4 3 5
        Output :
            5
            3
            4
            5
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, k = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a.sort()
        ans_index = min(k, n - 1)
        sys.stdout.write(str(a[ans_index]) + '\n')
