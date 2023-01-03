'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-03
    * Time : 6:39 a.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/MIXCOLOR)
        Chef likes to mix colors a lot. Recently, she was gifted N colors A1, A2, ..., AN by her friend.

        Chef wants to make the values of all her colors pairwise distinct, as they will then look stunningly
        beautiful. In order to achieve that, she can perform the following mixing operation zero or more times:

        Choose any two colors. Let's denote their values by x and y.
        Mix the color with value x into the color with value y. After the mixing, the value of the first color
        remains x, but the value of the second color changes to x + y.
        Find the minimum number of mixing operations Chef needs to perform to make her colors beautiful.
    * Example :
        Input :
            2
            3
            1 2 3
            3
            2 1 2
        Output :
            0
            1
'''
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=int(sys.stdin.readline().rstrip('\n'))
        arr=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        ans=len(arr)-len(set(arr))
        sys.stdout.write(str(ans)+'\n')
