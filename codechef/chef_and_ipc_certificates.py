'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-21
    * Time : 2:04 p.m.
    * Question :(https://www.codechef.com/LP1TO202/problems/IPCCERT)
        There were N students (numbered 1 through N) participating in the Indian Programming Camp (IPC) and they watched
        a total of K lectures (numbered 1 through K). For each student i and each lecture j, the i-th student watched
        the j-th lecture for T_{i, j} minutes.Additionally, for each student i, we know that this student asked the
        question, "What is the criteria for getting a certificate?" Q_i times.The criteria for getting a certificate is
        that a student must have watched at least M minutes of lectures in total and they must have asked the question
        no more than 10 times.Find out how many participants are eligible for a certificate.
    * Example :
        Input :
            4 8 4
            1 2 1 2 5
            3 5 1 3 4
            1 2 4 5 11
            1 1 1 3 12
        Ouytput :
            1
'''
import sys
if __name__=='__main__':
    n,m,k=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
    certi=0
    for i in range(n):
        T=[int(x) for x in sys.stdin.readline().rstrip('\n').split(' ')]
        q=T[-1]
        T=T[:-1]
        sum_ti=0
        for j in T:
            sum_ti+=j
        if sum_ti>=m and q<=10:
            certi+=1
    sys.stdout.write(str(certi)+'\n')