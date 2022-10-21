'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 12:46 a.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/MANYSUMS)
        You are given a range of integers {L,L+1,…,R}. An integer X is said to be reachable if it can be represented
        as a sum of two not necessarily distinct integers in this range. Find the number of distinct reachable integers.
    * Example :
        Input :
            2
            2 2
            2 3
        Output :
            1
            3
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        l,r=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        count=2*(r-l)+1
        sys.stdout.write(str(count)+'\n')
