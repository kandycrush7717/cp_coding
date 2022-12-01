'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-30
    * Time : 8:56 p.m.
    * Question :(https://www.codechef.com/LP1TO204/problems/STICKS)
        Chef and his little brother are playing with sticks. They have total N sticks. Length of i-th stick is A_i.
        Chef asks his brother to choose any four sticks and to make a rectangle with those sticks its sides.
        Chef warns his brother to not to break any of the sticks, he has to use sticks as a whole. Also, he wants
        that the rectangle formed should have the maximum possible area among all the rectangles that Chef's brother
        can make.
    * Example :
        Input :-
            2
            5
            1 2 3 1 2
            4
            1 2 2 3
        Output :-
            2
            -1
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip('\n'))
        a = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a_dct = dict(zip(set(a), [0] * len(set(a))))
        for i in a:
            a_dct[i] += 1
        a_dct = dict(sorted(a_dct.items(), key=lambda x: x[0], reverse=True))
        lb = []
        for i in a_dct:
            if len(lb) <= 2:
                if a_dct[i] >= 4:
                    lb.extend([i, i])
                elif a_dct[i] >= 2:
                    lb.append(i)
            else:
                break
        if len(lb) < 2:
            sys.stdout.write('-1\n')
        else:
            sys.stdout.write(str(lb[0] * lb[1]) + '\n')
