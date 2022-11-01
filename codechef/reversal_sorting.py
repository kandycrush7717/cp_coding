'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-01
    * Time : 2:22 a.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/REVSORT)
        Chef is deriving weird ways to sort his array. Currently he is trying to sort his arrays in increasing
        order by reversing some of his subarrays.
        To make it more challenging for himself, Chef decides that he can reverse only those subarrays that have
        sum of its elements at most X. Soon he notices that it might not be always possible to sort the array with
        this condition.

        Can you help the Chef by telling him if the given array can be sorted by reversing subarrays with sum at most X.

        More formally, for a given array AA and an integer X, check whether the array can be sorted in increasing
        order by reversing some (possibly none) of the subarrays such that the sum of all elements of the subarray
        is at most X.
    * Example :
        Input :
            3
            4 1
            1 2 3 4
            4 1
            2 1 3 4
            5 7
            3 2 2 3 3
        Output :
            YES
            NO
            YES
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        flag=True
        maxi=0
        for i in range(n):
            if maxi>a[i] and maxi+a[i]>k:
                flag=False
                break
            maxi=max(maxi,a[i])
        if flag:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
