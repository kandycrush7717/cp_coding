'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-03
    * Time : 11:31 a.m.
    * Question :(https://leetcode.com/problems/longest-common-prefix/)
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
    * Example :
        Input: strs = ["flower","flow","flight"]
        Output: "fl"
'''
import sys
def merge(s1,s2):
    common=""
    min_len=min(len(s1),len(s2))
    for i in range(min_len):
        if s1[i]!=s2[i]:
            return common
        common+=s1[i]
    return common
def longestCommonPrefix(a):
    if len(a)==1:
        return a[0]
    left=0
    right=len(a)
    mid=(left+right)//2
    return merge(longestCommonPrefix(a[left:mid]),longestCommonPrefix(a[mid,right]))
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        arr=[x for x in sys.stdin.readline().rstrip('\n').split()]
        c=longestCommonPrefix(arr)
        sys.stdout.write(c+'\n')

