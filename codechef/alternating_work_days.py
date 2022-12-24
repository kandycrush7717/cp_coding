'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-24
    * Time : 5:46 p.m.
    * Question :(https://www.codechef.com/LP2TO301/problems/ALTER)
        Alice and Bob are two friends. Initially, the skill levels of them are zero. They work on alternative days,
        i.e one of Alice and Bob works on the odd-numbered days(1,3,5,…) and the other works on the even-numbered
        days (2,4,6,…). The skill levels of Alice and Bob increase by A,B respectively on the days they work.

        Determine if it is possible that the skill levels of Alice and Bob become exactly P,Q respectively on some day.
    * Example :
        Input :
            4
            1 2 1 2
            1 2 3 2
            4 3 4 6
            3 5 9 25
        Output :
            YES
            NO
            YES
            NO
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        A,B,P,Q=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        if P%A==0 and Q%B==0 and abs((P//A)-(Q//B))<=1:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')