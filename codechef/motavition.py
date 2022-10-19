'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-19
    * Time : 2:52 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/IMDB)
        Chef has been searching for a good motivational movie that he can watch during his exam time.
        His hard disk has X GB of space remaining. His friend has NN movies represented with (S_i, R_i)(S_i,R_ i)
        representing (space required, IMDB rating). Help Chef choose the single best movie (highest IMDB rating)
        that can fit in his hard disk.
    * Example :
        Input :
            3
            1 1
            1 1
            2 2
            1 50
            2 100
            3 2
            1 51
            3 100
            2 50
        Output:
            1
            100
            51
'''
import sys
if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, x = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        tup_lst = []
        for i in range(n):
            a, b = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
            tup_lst.append((a, b))
        tup_lst.sort(key=lambda x: x[1], reverse=True)
        for i in tup_lst:
            if x >= i[0]:
                sys.stdout.write(str(i[1]) + '\n')
                break