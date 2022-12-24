'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-24
    * Time : 4:00 p.m.
    * Question :(https://www.codechef.com/LP2TO301/problems/INDIPERM)
        You are given an integer N. Construct an array P of size N such that:

        P is a permutation of the first N natural numbers, i.e, each integer 1,2,3,…N occurs exactly once in P. For
        example, [1, 3, 2] is a permutation of size 3, but [1, 3, 4] and [2, 1, 2] are not.
        P is indivisible. P is said to be indivisible if ii does not divide P_i or every index 2≤i≤N.
        It can be proven that under the given constraints, there always exists an indivisible permutation.
        If there are multiple, you may print any of them.
    * Example :
        Input :
            4
            2
            3
            4
            5
        Output :
            2 1
            1 3 2
            1 3 4 2
            4 5 2 3 1
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        N=int(sys.stdin.readline().rstrip('\n'))
        arr=[x for x in range(2,N+1)]
        arr.append(1)
        for i in arr:
            sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')