'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-20
    * Time : 11:50 p.m.
    * Question :
        No play and eating all day makes your belly fat. This happened to Chef during the lockdown. His weight before
        the lockdown was w_1kg (measured on the most accurate hospital machine) and after MM months of lockdown,
        when he measured his weight at home (on a regular scale, which can be inaccurate), he got the result that
        his weight was w_2kg (w_2>w_1).Scientific research in all growing kids shows that their weights increase
        by a value between x_1 and x_2kg (inclusive) per month, but not necessarily the same value each month.
        Chef assumes that he is a growing kid. Tell him whether his home scale could be giving correct results.
    * Example :
        Input :
            5
            1 2 1 2 2
            2 4 1 2 2
            4 8 1 2 2
            5 8 1 2 2
            1 100 1 2 2
        Output :
            0
            1
            1
            1
            0
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        w1,w2,x1,x2,m=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        diff=w2-w1
        max_val=m*max(x1,x2)
        min_val=m*min(x1,x2)
        if min_val<=diff<=max_val:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
