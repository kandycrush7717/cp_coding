'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-31
    * Time : 9:00 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/SIGNFLIP)
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
        a = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        max_sum = 0
        neg_lst = []
        for i in a:
            if i < 0:
                neg_lst.append(-1 * i)
            else:
                max_sum += i
        neg_lst.sort(reverse=True)
        min_len = min(k, len(neg_lst))
        for i in range(min_len):
            max_sum += neg_lst[i]
        sys.stdout.write(str(max_sum) + '\n')
