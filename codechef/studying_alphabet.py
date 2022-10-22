'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 6:00 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/ALPHABET)
        The first line of the input contains a lowercase Latin letter string S, consisting of the letters Jeff can
        read. Every letter will appear in S no more than once.
        The second line of the input contains an integer N denoting the number of words in the book.
        Each of the following N lines contains a single lowecase Latin letter string Wi, denoting the ith word in
        the book.
    * Example :
        Input :
            act
            2
            cat
            dog
        Output :
            Yes
            No
'''
import sys

if __name__ == '__main__':
    s = set([x for x in sys.stdin.readline().rstrip('\n')])
    n = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(n):
        s1 = set(list(sys.stdin.readline().rstrip('\n')))
        flag = True
        for i in s1:
            if i not in s:
                flag = False
                break
        if flag:
            sys.stdout.write('Yes\n')
        else:
            sys.stdout.write('No\n')

