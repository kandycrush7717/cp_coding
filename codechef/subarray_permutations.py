'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-02
    * Time : 8:02 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/SUBPERM)
        A permutation of length NN is an array of NN integers P = [P_1, P_2,..., P_N] such that every integer from
        1 to N (inclusive) appears in it exactly once. For example, [2, 3, 4, 1] is a permutation of length 4.
        A subsegment of an array A[L...R]=[A_L, A_{L+1},...., A_{R} is called good if the subsegment is a permutation
        of length (R-L+1). For example, the array A = [2, 3, 1, 4, 2] contains 33 good subsegments:
        A[3…3]=[1],A[1…3]=[2,3,1],A[2…5]=[3,1,4,2].
        You are given two integers N and K. Find a permutation of length N such that it contains exactly K good
        subsegments. Print -1 if no such permutation exists.
    * Example :
        Input :-
            4
            1 1
            3 2
            4 1
            5 3
        Output :-
            1
            1 3 2
            -1
            5 3 1 4 2
'''
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        N,K=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        arr=[i for i in range(1,N+1)]
        x=N-K+1
        if N>=2 and K==1:
            print(-1)
        else:
            if 1<=x<=N:
                arr[N-x:N]=arr[-1:-1-x:-1]
                for i in arr:
                    sys.stdout.write(str(i)+' ')
                sys.stdout.write('\n')
            else:
                print(-1)
