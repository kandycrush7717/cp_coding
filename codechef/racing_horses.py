'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-01
    * Time : 12:14 a.m.
    * Question :(https://www.codechef.com/LP1TO204/problems/HORSES)
        There are N horses in the stable. The skill of the horse i is represented by an integer S[i]. The Chef needs
        to pick 2 horses for the race such that the difference in their skills is minimum. This way, he would be
        able to host a very interesting race. Your task is to help him do this and report the minimum difference
        that is possible between 2 horses in the race.
    * Example :
        Input :-
            1
            5
            4 9 1 32 13
        Output :-
            3
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        s=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        s.sort()
        min_diff=(10**9)+7
        for i in range(0,n-1):
            min_diff=min(min_diff,s[i+1]-s[i])
        sys.stdout.write(str(min_diff)+'\n')