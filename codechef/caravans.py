'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 5:44 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/CARVANS)
        Formally, you're given the maximum speed of N cars in the order they entered the long straight segment of
        the circuit. Each car prefers to move at its maximum speed. If that's not possible because of the front car
        being slow, it might have to lower its speed. It still moves at the fastest possible speed while avoiding any
        collisions. For the purpose of this problem, you can assume that the straight segment is infinitely long.
        Count the number of cars which were moving at their maximum speed on the straight segment.
    * Example :
        Input :
            3
            1
            10
            3
            8 3 6
            5
            4 5 1 2 3
        Output :
            1
            2
            2
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        speed=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        count=1
        max_speed=speed[0]
        for i in range(1,n):
            if speed[i]<=max_speed:
                count+=1
                max_speed=speed[i]
        sys.stdout.write(str(count)+'\n')
