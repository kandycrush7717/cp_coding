'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-05
    * Time : 7:03 p.m.
    * Question :(https://leetcode.com/problems/valid-palindrome-ii/)
        Given a string s, return true if the s can be palindrome after deleting at most one character from it.
    * Example :
        Input: s = "abca"
        Output: true
        Explanation: You could delete the character 'c'.
'''
import sys
def checkPalindrome(s,i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def validPalindrome(s):
    i=0
    j=len(s)-1
    while(i<j):
        if s[i]!=s[j]:
            return checkPalindrome(s,i,j-1) or checkPalindrome(s,i+1,j)
        i+=1
        j-=1
    return True
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        flag=validPalindrome(s)
        sys.stdout.write(str(flag)+'\n')

'''
            Recursive Approach
def validSkipPalindrome(s,skip):
    if len(s)==0 or len(s)==1:
        return True
    if s[i]==s[j]:
        return validSkipPalindrome(s[1:-1],skip)
    else:
        return self.validSkipPalindrome(s[1:],1) or self.validSkipPalindrome(s[:-1],1) if skip==0 else False
def validPalindrome(s):
    return validSkipPalindrome(s,0)
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        s=sys.stdin.readline().rstrip('\n')
        flag=validPalindrome(s)
        sys.stdout.write(str(flag)+'\n')

'''

