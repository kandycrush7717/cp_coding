'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 3:50 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/BEGGASOL)
        There are N cars (numbered 1 through N) on a circular track with length N. For each i (2≤i≤N), the i-th of them
        is at a distance i−1 clockwise from car 1, i.e. car 1 needs to travel a distance i−1 clockwise to reach car i.
        Also, for each valid i, the i-th car has f_i litres of gasoline in it initially.
        You are driving car 1 in the clockwise direction. To move one unit of distance in this direction, you need to
        spend 1 litre of gasoline. When you pass another car (even if you'd run out of gasoline exactly at that point),
        you steal all its gasoline. Once you do not have any gasoline left, you stop.
        What is the total clockwise distance travelled by your car?
    * Example :
        Input :
            3
            5
            3 0 0 0 0
            5
            1 1 1 1 1
            5
            5 4 3 2 1
        Output :
            3
            5
            15
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n = int(sys.stdin.readline().rstrip('\n'))
        f = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        fuel = f[0]
        distance = 0
        for i in range(1, n):
            if fuel >= 1:
                fuel += (f[i] - 1)
                distance += 1
            else:
                break
        distance += fuel
        sys.stdout.write(str(distance) + '\n')
