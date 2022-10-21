'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 2:16 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/MAKEEQUAL)
        Chef has an array A having N elements. Chef wants to make all the elements of the array equal by repeating
        the following move.Choose any integer K between 1 and N (inclusive). Then choose K distinct indices
        i_1 , i_2,...., i_K and increase the values of A_{i_1} , A_{i_2} ,...., A_{i_K}  by 1.
        Find the minimum number of moves required to make all the elements of the array equal.
    * Example :
        Input :
            2
            3
            1 3 1
            3
            2 2 2
        Output :
            2
            0
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        min_a=min(a)
        max_a=max(a)
        res=max_a-min_a
        sys.stdout.write(str(res)+'\n')