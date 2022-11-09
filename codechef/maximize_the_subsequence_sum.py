'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-09
    * Time : 4:27 p.m.
    * Question :(https://www.codechef.com/LP1TO204/problems/SIGNFLIP)
        Chef has an array A containing N integers. The integers of the array can be positive, negative, or even zero.
        Chef allows you to choose at most K elements of the array and multiply them by -1.
        Find the maximum sum of a subsequence you can obtain if you choose the elements of the subsequence optimally.
    * Example :
        Input :
            3
            6 2
            6 -10 -1 0 -4 2
            5 0
            -1 -1 -1 -1 -1
            3 3
            1 2 3
        Output :
            22
            0
            6
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, k = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        arr = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        tsum = 0
        neg_lst = [abs(i) for i in arr if i < 0]
        neg_lst.sort(reverse=True)
        pos_lst = [i for i in arr if i > 0]
        pos_lst.sort(reverse=True)
        pos_lst.extend(neg_lst[:k])
        for i in pos_lst:
            tsum += i
        sys.stdout.write(str(tsum) + '\n')
