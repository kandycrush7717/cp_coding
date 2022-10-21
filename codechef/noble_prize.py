'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 7:07 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/NOBEL)
        The growth of Computer Science has forced the scientific community to award Nobel Prize in CS starting from this
         year.
         Chef knows that the Nobel community is going to award the prize to that person whose research is different from
         others (ie. no other researcher should work on the same topic). If there are multiple such people, who work
         on unique topics, then they will all share the prize. It might also happen that no one wins this time.
         Chef also knows the NN researchers which the community who will be considered for the prize, and the topics
         in which each of them work.
         In total the CS field can be divided into M broad topics. Given the topics in which each of the N researchers
         are working on, in the form of an array A, and given that Chef can master any topic instantly, find whether
         he can win the prize. That is, can the Chef choose to work on some topic which will guarantee that he will
         win the prize? Chef doesn't mind sharing the prize with others.
    * Example :
        Input :
            3
            4 4
            1 2 3 4
            5 4
            4 2 1 1 1
            4 4
            4 4 4 4
        Output :
            No
            Yes
            Yes
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, m = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        a = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        unique = set(a)
        if len(unique) < m:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')