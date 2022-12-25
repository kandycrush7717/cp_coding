'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-12-24
    * Time : 7:09 p.m.
    * Question :(https://leetcode.com/problems/search-in-rotated-sorted-array/)
        There is an integer array nums sorted in ascending order (with distinct values).

        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
        such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed)
        For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer target, return the index of target if it is in
        nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.
    * Example :
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
'''
import sys

def binSearch(arr,target:int,left:int,right:int)->int:
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif ans[left]<=arr[mid]:
        if target>arr[mid] or target<arr[left]:
            return binSearch(arr,target,mid+1,right)
        else:
            return binSearch(arr,target,left,mid)
    else:
        if target<arr[mid] or target>arr[right]:
            return binSearch(arr,target,left,mid)
        else:
            return binSearch(arr,target,mid+2,right)

def search(arr,target:int)->int:
    return binSearch(arr,target,0,len(arr)-1)

if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        arr=[int(x) for x in sys.stdin.readline().rstrip('\n').split()]
        target=int(sys.stdin.readline().rstrip('\n'))
        ans=search(arr,target)
        sys.stdout.write(str(ans)+'\n')