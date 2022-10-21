'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 1:10 a.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/TANDJ1)
        There is a grid of size 10^5 times 10^5, covered completely in railway tracks. Tom is riding in a train,
        currently in cell (a,b), and Jerry is tied up in a different cell (c,d), unable to move. The train has no
        breaks. It shall move exactly KK steps, and then its fuel will run out and it shall stop. In one step, the
        train must move to one of its neighboring cells, sharing a side. Tom can’t move without the train, as the grid
        is covered in tracks. Can Tom reach Jerry’s cell after exactly K steps?

        Note: Tom can go back to the same cell multiple times.
    * Example :
        Input :
            3
            1 1 2 2 2
            1 1 2 3 4
            1 1 1 0 3
        Output :
            YES
            NO
            YES
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a,b,c,d,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        steps=abs(a-c)+abs(b-d)
        if steps>k:
            sys.stdout.write('NO\n')
        else:
            if (k-steps)%2==0:
                sys.stdout.write('YES\n')
            else:
                sys.stdout.write('NO\n')
