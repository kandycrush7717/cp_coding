'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-07
    * Time : 11:57 a.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/MXMEDIAN)
        You are given an array A of size 2 * N consisting of positive integers, where N is an odd number. You can construct
        an array B from A as follows, B[i] = max(A[2 * i - 1], A[2 * i]), i.e. B array contains the maximum of adjacent
        pairs of array A. Assume that we use 1-based indexing throughout the problem.

        You want to maximize the median of the array B. For achieving that, you are allowed to permute the entries of A.
        Find out the maximum median of corresponding B array that you can get. Also, find out any permutation for which
        this maximum is achieved.
    * Example :
        Input :
            3
            1
            1 2
            3
            1 2 3 4 5 6
            3
            1 3 3 3 2 2
        Output :
            2
            1 2
            5
            1 3 2 5 4 6
            3
            1 3 3 3 2 2
'''
import sys
import math

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip())
        arr=[int(x) for x in sys.stdin.readline().rstrip().split()]
        arr.sort()
        b_median=arr[n-1+int(math.ceil(n/2))]
        i=0
        j=n
        per=[0]*(2*n)
        k=0
        while(i<n):
            per[k]=arr[i]
            k+=1
            per[k]=arr[j]
            k+=1
            i+=1
            j+=1
        sys.stdout.write(str(b_median)+'\n')
        for i in per:
            sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')