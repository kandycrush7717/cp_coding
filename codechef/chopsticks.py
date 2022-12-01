'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-30
    * Time : 8:13 p.m.
    * Question :(https://www.codechef.com/LP1TO204/problems/TACHSTCK)
        Actually, the two sticks in a pair of chopsticks need not be of the same length. A pair of sticks can be used
        to eat as long as the difference in their length is at most D. The Chef has N sticks in which the ith stick is
        L[i] units long. A stick can't be part of more than one pair of chopsticks. Help the Chef in pairing up the
        sticks to form the maximum number of usable pairs of chopsticks.
    * Example :
        Input :-
            5 2
            1
            3
            3
            9
            4
        Output :-
            2
'''
import sys

if __name__ == '__main__':
    n, d = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
    l = []
    for _ in range(n):
        l.append(int(sys.stdin.readline().rstrip('\n')))
    l.sort()
    ans = 0
    for i in range(0, len(l) - 1):
        if l[i] != -1 and l[i + 1] - l[i] <= d:
            ans += 1
            l[i] = -1
            l[i + 1] = -1
    sys.stdout.write(str(ans) + '\n')