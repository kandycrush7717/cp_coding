'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-01
    * Time : 6:15 p.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/POLYREL)
        You are given a strictly convex polygon with N vertices (numbered 1 through N). For each valid i, the
        coordinates of the i-th vertex are (X_i ,Y_i). You may perform the following operation any number of times (
        including zero):

        Consider a parent polygon. Initially, this is the polygon you are given.
        Draw one of its child polygons ― a simple non-degenerate polygon such that each of its sides is a chord of the
        parent polygon (it cannot be a side of the parent polygon). The operation cannot be performed if the parent
        polygon does not have any child polygons.
        The child polygon which you drew becomes the new parent polygon.
        Your goal is to draw as many sides of polygons in total as possible (including the polygon given at the start).
        Find this maximum total number of sides.
    * Example :
        Input :
            2
            4
            -100 1
            0 2
            0 0
            100 1
            7
            -4 0
            -3 -2
            -3 2
            0 -4
            2 -3
            2 3
            3 2
        Output :
            4
            10
'''
import sys
import math

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip())
        points = []
        for i in range(n):
            points.append(sys.stdin.readline().rstrip())
        sides = n
        while True:
            chord_points = 0
            if n & 1 == 0:
                chord_points = n // 2
            else:
                chord_points = int(math.floor(n / 2))
            if chord_points < 3:
                break
            n = chord_points
            sides += n
        sys.stdout.write(str(sides) + '\n')