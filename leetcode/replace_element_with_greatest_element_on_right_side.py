'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-02
    * Time : 7:07 p.m.
    * Question :(https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)
        Given an array arr, replace every element in that array with the greatest element among the elements to
        its right, and replace the last element with -1.
    * Example :
        Input: arr = [17,18,5,4,6,1]
        Output: [18,6,6,6,1,-1]
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        arr=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        n=len(arr)
        maxi=arr[n-1]
        ans=[-1]
        for i in range(n-2,-1,-1):
            ans.append(maxi)
            maxi=max(maxi,arr[i])
        ans=ans[::-1]
        print(ans)
