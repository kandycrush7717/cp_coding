'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 3:20 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/SUBTASK)
        Chef recently solved his first problem on CodeChef. The problem he solved has N test cases. He gets a score for his submission according to the following rules:
            1.If Chef’s code passes all the N test cases, he gets 100 points.

            2.If Chef’s code does not pass all the test cases, but passes all the first M(M<N) test cases, he gets K(K<100) points.

            3.If the conditions 1 and 2 are not satisfied, Chef does not get any points (i.e his score remains at 0 points).
        You are given a binary array A_1, A_2,..., A_N of length N, where A_i = 1 denotes Chef's code passed the
        ith test case, A_i = 0 denotes otherwise. You are also given the two integers M,,K. Can you find how many
        points does Chef get?
    * Example :
        Input :
            4
            4 2 50
            1 0 1 1
            3 2 50
            1 1 0
            4 2 50
            1 1 1 1
            5 3 30
            1 1 0 1 1
        Output :
            0
            50
            100
            0
'''
import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        n, m, k = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        a = [int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        passed = 0
        for i in a:
            if i == 1:
                passed += 1
            else:
                break
        if passed == n:
            sys.stdout.write('100\n')
        elif passed >= m:
            sys.stdout.write(str(k) + '\n')
        else:
            sys.stdout.write('0\n')
