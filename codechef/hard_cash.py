'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 6:10 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/CASH)
        Chef wants to take Chefina on a date. However, he has to complete one more task before leaving. Since he does
        not want to be late, he is asking you for help.
        There are N bags with coins in a row (numbered 1 through N); for each valid i, the i-th bag contains A_i coins.
        Chef should make the number of coins in each bag divisible by a given integer K in the following way:

            choose an integer c between 0 and N (inclusive)
            take some coins from the first c bags ― formally, for each i(1≤i≤c), he may choose any number of coins
            between 0 and A_i inclusive and take them out of the i-th bag move some of these coins to some of the
            last N-c bags ― formally, for each i (c+1≤i≤N), he may place a non-negative number of coins in the i-th
            bag Of course, the number of coins placed in the last N-c bags must not exceed the number of coins
            taken out from the first c bags, but there may be some coins left over. Let's denote the number of these
            coins by R. You should find the smallest possible value of R.
    * Example :
        Input :
            2
            5 7
            1 14 4 41 1
            3 9
            1 10 19
        Output :
            5
            3
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, k = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        coins = [int(x) % k for x in sys.stdin.readline().rstrip('\n').split(' ')]
        total_req_coins = 0
        for i in coins:
            total_req_coins += (k - i)
        front_sum = 0
        min_diff = (10 ** 9) + 1
        for i in coins:
            front_sum += i
            total_req_coins -= (k - i)
            if front_sum >= total_req_coins:
                temp = front_sum - total_req_coins
                if temp < min_diff:
                    min_diff = temp
        sys.stdout.write(str(min_diff) + '\n')