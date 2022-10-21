'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-20
    * Time : 11:11 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/NFS)
        Chef is playing Need For Speed. Currently, his car is running on a straight road with a velocity U metres
        per second and approaching a 90∘ turn which is S metres away from him. To successfully cross the turn,
        velocity of the car when entering the turn must not exceed V metres per second.
        The brakes of Chef's car allow him to slow down with a deceleration (negative acceleration) not exceeding A
        metres per squared second. Tell him whether he can cross the turn successfully. The velocity v when entering
        the turn can be determined from Newton's 2nd law to be v^2 = U^2 + 2*a*S if the car is moving with a uniform
        acceleration a.
    * Example :
        Input :
            3
            1 1 1 1
            2 1 1 1
            2 2 1 1
        Output :
            Yes
            No
            Yes
'''
import sys
import math

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        u, v, a, s = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        res = (u * u) - (2 * a * s)
        if res <= 0:
            sys.stdout.write('YES\n')
        elif math.sqrt(res) <= v:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')

