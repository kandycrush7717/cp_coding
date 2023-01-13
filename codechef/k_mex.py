'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-12
    * Time : 11:24 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/KMEX)
        You are given an array A containing N integers. Find if it is possible to choose exactly M elements from the
        array such that the MEX of the chosen elements is exactly K.

        Recall that the MEX of an array is the smallest non-negative integer that does not belong to the array. For
        example, the MEX of [2,2,1] is 0 because 0 does not belong to the array, the MEX of [3,1,0,1] is 2 because
        0 and 1 belong to the array, but 2 does not.
    * Example :
        Input :
            6
            5 4 2
            0 1 3 0 3
            2 1 2
            0 1
            3 3 3
            0 1 2
            4 3 3
            2 0 4 3
            5 4 2
            0 2 1 2 5
            6 5 2
            0 1 0 2 0 3
        Output :
            YES
            NO
            YES
            NO
            NO
            YES
'''
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,m,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        if m<k:
            sys.stdout.write('No\n')
        else:
            g_nums=[]
            l_nums=[]
            req_nums=[x for x in range(k)]
            for i in a:
                if i<k:
                    l_nums.append(i)
                elif i>k:
                    g_nums.append(i)
            if set(l_nums)==set(req_nums):
                if m==k:
                    sys.stdout.write('Yes\n')
                else:
                    if len(l_nums)+len(g_nums)>=m:
                        sys.stdout.write('Yes\n')
                    else:
                        sys.stdout.write('No\n')
            else:
                sys.stdout.write('No\n')