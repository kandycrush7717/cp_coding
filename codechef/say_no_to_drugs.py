'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-01-03
    * Time : 7:18 a.m.
    * Question :(https://www.codechef.com/LP2TO308/problems/NODRUGS)
        There are N people participating in a race. The N_th participant is your friend, so you want him to win.
        You are not a man of ethics, so you decided to inject some units of a Performance Enhancement \
        Drug (don't ask where that came from) in your friend's body.

        From the charts, you came to know the speed of every player. Formally, for a player i, his speed is denoted
        by S_i
        The change in speed with one unit of the drug is K units. Note that K can be negative, which means the drug
        has more side effects than benefits.
        Of course, there will be a drug test before the race, so your friend will be caught if the number of units of
        the drug in his blood is greater than or equal to L.
        You need to determine whether you can help your friend to win the race (with or without drugs), without getting
        caught.

        Note: A player wins the race if he has the maximum speed among all the participants. If there are more than
        one people with a maximal speed, they tie at first place, and no one wins!
    * Example :
        Input :
            3
            4 2 2
            2 1 3 2
            4 2 2
            2 1 4 2
            3 -10 100
            12 11 9
        Output :
            Yes
            No
            No
'''
import sys
import math

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, k, l = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        arr_n = [int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        maxi = max(arr_n)
        nth = arr_n[-1]
        count_max = 0
        req_units = 0
        for i in arr_n:
            if i == maxi:
                count_max += 1
        if k <= 0:
            if count_max == 1 and nth == maxi:
                print('Yes')
            else:
                print('No')
        else:
            nth += (k * (l - 1))
            if nth > maxi:
                print('Yes')
            else:
                print('No')
            # req_units=int(math.ceil((maxi+1-nth)/k))
            # if req_units<l:
            #     print('Yes')
            # else:
            #     print('No')