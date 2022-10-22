'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-22
    * Time : 6:35 p.m.
    * Question :(https://www.codechef.com/LP1TO203/problems/LAPIN)
        Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters
        and same frequency of each character. If there are odd number of characters in the string, we ignore the
        middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga
        have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes.
        Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not
        match.
        Your task is simple. Given a string, you need to tell if it is a lapindrome.
    * Example :
        Input :
            6
            gaga
            abcde
            rotor
            xyzxy
            abbaab
            ababc
        Output :
            YES
            NO
            YES
            YES
            NO
            NO
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        hf_len=len(s)//2
        freq_dict={}
        for i in range(hf_len):
            if s[i] in freq_dict:
                freq_dict[s[i]]+=1
            else:
                freq_dict[s[i]]=1
        s=s[::-1]
        flag=True
        for i in range(hf_len):
            if s[i] in freq_dict:
                freq_dict[s[i]]-=1
            else:
                flag=False
        for i in freq_dict:
            if freq_dict[i]!=0:
                flag=False
                break
        if flag:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')