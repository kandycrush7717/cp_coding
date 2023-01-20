'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-20
    * Time : 1:40 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/LARGEFAM)
        A certain parallel universe has exactly N people living in it.
        The i-th of these N people claims that they are the parent of exactly A_i of these N people.
        However, some of these people might be lying — the i-th person may be either telling the truth (in which case
        they have exactly A_i children) or lying (in which case they can have any number of children).
        It is known that each person has at most one parent. Further, as one would expect, it is not allowed for a
        person's child to also be their ancestor.
        What is the maximum possible number of truth-tellers in this universe?
    * Example :
        Input :
            4
            2
            1 0
            2
            1 1
            3
            2 0 1
            5
            2 3 1 2 3
        Output :
            2
            1
            2
            2
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        arr = [int(x) for x in sys.stdin.readline().rstrip().split()]
        arr.sort()
        tot = 0
        ans = -1
        for i, e in enumerate(arr):
            if tot + e <= n - 1:
                tot += e
                ans = i
            else:
                break
        print(ans + 1)

