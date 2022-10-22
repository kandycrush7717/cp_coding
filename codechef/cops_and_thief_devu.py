'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 8:04 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/COPS)
        There are 100 houses located on a straight line. The first house is numbered 1 and the last one is numbered 100.
        Some M houses out of these 100 are occupied by cops.
        Thief Devu has just stolen PeePee's bag and is looking for a house to hide in.
        PeePee uses fast 4G Internet and sends the message to all the cops that a thief named Devu has just stolen her
        bag and ran into some house.
        Devu knows that the cops run at a maximum speed of x houses per minute in a straight line and they will search
        for a maximum of y minutes. Devu wants to know how many houses are safe for him to escape from the cops. Help
        him in getting this information.
    * Example :
        Input :
            3
            4 7 8
            12 52 56 8
            2 10 2
            21 75
            2 5 8
            10 51
        Output :
            0
            18
            9
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        m, x, y = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        arr = [0 for i in range(102)]
        cops = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        for i in cops:
            if i - (x * y) <= 0:
                arr[1] -= 1
            else:
                arr[i - (x * y)] -= 1
            if i + (x * y) < 100:
                arr[i + (x * y) + 1] += 1
        tot_sum = 0
        count = 0
        for i in range(1, 101):
            tot_sum += arr[i]
            arr[i] = tot_sum
            if arr[i] == 0:
                count += 1
        sys.stdout.write(str(count) + '\n')
