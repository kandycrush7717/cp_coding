'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-30
    * Time : 4:55 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/GFTSHP)
        Chef wants to impress Chefina by giving her the maximum number of gifts possible.
        Chef is in a gift shop having NN items where the cost of the i_th item is equal to A_{i} Chef has K amount of
        money and a 50% off discount coupon that he can use for at most one of the items he buys.
        If the cost of an item is equal to X, then, after applying the coupon on that item, Chef only has to
        pay ⌈X/2⌉ (rounded up to the nearest integer) amount for that item.
        Help Chef find the maximum number of items he can buy with K amount of money and a 50% discount coupon
        given that he can use the coupon on at most one item.
    * Example :
        Input :
            3
            1 4
            5
            3 15
            4 4 5
            3 10
            6 7 4
        Output :
            1
            3
            2
'''
import sys
import math

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, k = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        a.sort()
        count = 0
        for i in range(n):
            if k >= a[i]:
                k -= a[i]
                count += 1
            else:
                if k >= int(math.ceil(a[i] / 2)):
                    count += 1
                break
        sys.stdout.write(str(count) + '\n')