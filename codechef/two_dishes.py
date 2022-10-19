'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-19
    * Time : 3:31 p.m.
    * Question :(https://www.codechef.com/LP1TO201/problems/TWODISH)
        Chef will have NN guests in his house today. He wants to serve at least one dish to each of the NN guests.
        Chef can make two types of dishes. He needs one fruit and one vegetable to make the first type of dish and one
        vegetable and one fish to make the second type of dish. Now Chef has AA fruits, BB vegetables, and CC fishes in
        his house. Can he prepare at least NN dishes in total?
    * Example :
        Input :
            4
            2 1 2 1
            3 2 2 2
            4 2 6 3
            3 1 3 1
        Output:
            YES
            NO
            YES
            NO
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,a,b,c=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        dishes=0
        dishes+=min(a,b)
        b-=dishes
        dishes+=min(b,c)
        if dishes>=n:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
