'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-11
    * Time : 11:15 p.m.
    * Question :(https://leetcode.com/problems/k-closest-points-to-origin/)
        Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
        return the k closest points to the origin (0, 0).
        The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
        You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
    * Example :
        Input: points = [[1,3],[-2,2]], k = 1
        Output: [[-2,2]]
        Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
'''
import sys
import math
if __name__=='__main__':
    points=[list(x) for x in sys.stdin.readline().rstrip('\n').split(',')]
    k=int(sys.stdin.readline().rstrip('\n'))
    point_lst=[]
    for i in points:
        key=math.sqrt((i[1]**2)+(i[0]**2))
        point_lst.append((key,i))
    point_lst.sort(key=lambda x:x[0])
    min_len=min(len(point_lst),k)
    for i in range(min_len):
        sys.stdout.write(str((point_lst[i])[1])+' ')
    sys.stdout.write('\n')