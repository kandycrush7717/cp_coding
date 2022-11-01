'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-31
    * Time : 8:31 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/POLIN)
        Given N points of the form (x_i, y_i) on a 22-D plane.
        From each point, you draw 2 lines one horizontal and one vertical. Now some of the lines may overlap each
        other, therefore you are required to print the number of distinct lines you can see on the plane.
    * Example :
        Input:
            3
            4
            1 1
            1 0
            0 1
            0 0
            5
            0 0
            0 1
            0 2
            0 3
            0 4
            1
            10 10
        Output :
            4
            6
            2

'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip('\n'))
        points = []
        tot_line = 0
        for i in range(n):
            a, b = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
            points.append((a, b))
        tot_lines = (n * 2)
        unique_x_len = len(set([x[0] for x in points]))
        unique_y_len = len(set([x[1] for x in points]))
        tot_lines -= (n - unique_x_len)
        tot_lines -= (n - unique_y_len)
        sys.stdout.write(str(tot_lines) + '\n')
