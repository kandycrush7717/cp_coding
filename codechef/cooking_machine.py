'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-01
    * Time : 12:16 a.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/COOKMACH)
        Chef is on a vacation these days, so his friend Chefza is trying to solve Chef's everyday tasks.

        Today's task is to make a sweet roll. Rolls are made by a newly invented cooking machine. The machine is
        pretty universal - it can make lots of dishes and Chefza is thrilled about this.

        To make a roll, Chefza has to set all the settings to specified integer values. There are lots of settings,
        each of them set to some initial value. The machine is pretty complex and there is a lot of cooking to be
        done today, so Chefza has decided to use only two quick ways to change the settings. In a unit of time, he
        can pick one setting (let's say its current value is v) and change it in one of the following ways.

        If v is even, change this setting to v/2. If v is odd, change it to (v − 1)/2.
        Change setting to 2 × v
        The receipt is given as a list of integer values the settings should be set to. It is guaranteed that
        each destination setting can be represented as an integer power of 2.

        Since Chefza has just changed his profession, he has a lot of other things to do. Please help him find
        the minimum number of operations needed to set up a particular setting of the machine. You can prove that
        it can be done in finite time.
    * Example :
        Input :
            6
            1 1
            2 4
            3 8
            4 16
            4 1
            1 4
        Output :
            0
            1
            4
            2
            2
            2
'''
import sys


def getVal(x):
    count = 0
    pos = 0
    pos_1_lst = []
    while (x > 0):
        if (x & 1) != 0:
            count += 1
            pos_1_lst.append(pos + 1)
        pos += 1
        x >>= 1
    if len(pos_1_lst) >= 2:
        return pos_1_lst[-2], pos, count
    return 0, pos, count


if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        a, b = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        sl_a_msb_1, a_msb_1, a_count_1 = getVal(a)
        sl_b_msb_1, b_msb_1, b_count_1 = getVal(b)
        ans = 0
        if a_count_1 == 1:
            ans = abs(b_msb_1 - a_msb_1)
        else:
            ans += sl_a_msb_1
            a_msb_1 -= sl_a_msb_1
            ans += abs(b_msb_1 - a_msb_1)
        sys.stdout.write(str(ans) + '\n')
'''
A Different Approach
for _ in range(int(input())):
    a, b = map(int, input().split())
    count = 0
    while(b % a != 0):
        a >>= 1
        count += 1
    while(a != b):
        a <<= 1
        count += 1
    print(count)
'''
