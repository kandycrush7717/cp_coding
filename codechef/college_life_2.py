'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 7:27 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/COLGLF2)
        Chef has just started watching Game of Thrones, and he wants to first calculate the exact time (in minutes)
        that it'll take him to complete the series.The series has S seasons, and the ith season has E_i episodes, each
        of which are L_{i,1}, L_{i,2},..., L_{i,E_i} minutes long. Note that these L_{i,j} include the duration
        of the beginning intro song in each episode. The streaming service that he uses, allows Chef to skip the
        intro song. The intro song changes slightly each season, and so he wants to watch the intro song in the
        first episode of each season, but he'll skip it in all other episodes of that season (yes, we know, a sacrilege!).
        You know that the intro song lasts for Q_i minutes in the i th season.Find the total time in minutes,
        that he has to watch.
    * Example :
        Input :
            2
            1
            10
            5 11 11 11 11 11
            5
            10 10 10 10 10
            1 11
            1 11
            1 11
            1 11
            1 11
        Output :
            15
            55
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        time = 0
        s = int(sys.stdin.readline().rstrip('\n'))
        q = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        for i in range(s):
            e = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
            l = e[1:]
            e = e[0]
            time += sum(l)
            time -= ((e - 1) * q[i])
        sys.stdout.write(str(time) + '\n')

