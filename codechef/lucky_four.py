'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-12
    * Time : 1:54 a.m.
    * Question :(https://www.codechef.com/LP0TO101/problems/LUCKFOUR)
        Impressed by the power of this number, Kostya has begun to look for occurrences of four anywhere.
        He has a list of T integers, for each of them he wants to calculate the number of occurrences of the digit
        4 in the decimal representation. He is too busy now, so please help him.
    * Example :
        Input:
        5
        447474
        228
        6664
        40
        81
        Output:
        4
        0
        1
        1
        0
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n=sys.stdin.readline().rstrip('\n')
        count=0
        for i in n:
            if i=='4':
                count+=1
        sys.stdout.write(str(count)+'\n')
