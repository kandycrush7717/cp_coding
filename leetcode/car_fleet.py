'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-20
    * Time : 2:45 p.m.
    * Question :(https://leetcode.com/problems/car-fleet/)
        There are n cars going to the same destination along a one-lane road. The destination is target miles away.

        You are given two integer array position and speed, both of length n, where position[i] is the position of the
        ith car and speed[i] is the speed of the ith car (in miles per hour).

        A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same
        speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is
        ignored (i.e., they are assumed to have the same position).

        A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is
        also a car fleet.

        If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

        Return the number of car fleets that will arrive at the destination.
    * Example :
        Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        Output: 3
'''


def carFleet(self, target: int, position, speed):
    fleets = 0
    ps = [(p, s) for p, s in zip(position, speed)]
    ps.sort(key=lambda x: x[0], reverse=True)
    stk = []
    for i in range(len(position)):
        p, s = ps[i]
        curr_time = (target - p) / s
        if len(stk) > 0 and stk[-1] < curr_time:
            stk.clear()
            fleets += 1
        stk.append(max(stk[-1] if len(stk) > 0 else curr_time, curr_time))
    return fleets + 1 if len(stk) > 0 else fleets
