'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-28
    * Time : 3:26 p.m.
    * Question :(https://www.codechef.com/LP1TO205/problems/HOLIDAYS)
        Ved is a salesman. He needs to earn at least W rupees in NN days for his livelihood. However, on a given day
        i (1≤i≤N), he can only earn A_i rupees by working on that day.
        Ved, being a lazy salesman, wants to take as many holidays as possible. It is known that on a holiday,
        Ved does not work and thus does not earn anything. Help maximize the number of days on which Ved can
        take a holiday.
        It is guaranteed that Ved can always earn at least W rupees by working on all days.
    * Example :
        Input :
            3
            5 10
            3 2 6 1 3
            4 15
            3 2 4 6
            6 8
            9 12 6 5 2 2
        Output :
            2
            0
            5
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, w = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        a = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        a.sort(reverse=True)
        ans = n
        for i in a:
            if w <= 0:
                break;
            w -= i
            ans -= 1
        sys.stdout.write(str(ans) + '\n')

