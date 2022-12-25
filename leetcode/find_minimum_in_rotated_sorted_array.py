'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-24
    * Time : 8:21 p.m.
    * Question :(https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
        Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the
        array nums = [0,1,2,4,5,6,7] might become:

        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1],
        a[2], ..., a[n-2]].

        Given the sorted rotated array nums of unique elements, return the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.
    * Example :
        Input: nums = [3,4,5,1,2]
        Output: 1
        Explanation: The original array was [1,2,3,4,5] rotated 3 times.
'''
import sys
def modifiedBinSearch(arr,left,right,mini):
    if arr[left]<=arr[right]:
        return min(mini,arr[left])
    mid=(left+right)//2
    mini=min(mini,arr[mid])
    if arr[mid]>=arr[left]:
        return modifiedBinSearch(arr,mid+1,right,mini)
    else:
        return modifiedBinSearch(arr,left,mid-1,mini)

def searchMin(arr):
    return modifiedBinSearch(arr,0,len(arr)-1,arr[0])

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        arr=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        ans=searchMin(arr)
        sys.stdout.write(str(ans)+'\n')