'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-20
    * Time : 1:26 p.m.
    * Question :(https://leetcode.com/problems/daily-temperatures/)
        Given an array of integers temperatures represents the daily temperatures, return an array answer such that
        answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no
        future day for which this is possible, keep answer[i] == 0 instead.
    * Example :
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
'''


def dailyTemperatures(self, temperatures):
    ans = [0] * len(temperatures)
    stk = []
    for i, t in enumerate(temperatures):
        while (len(stk) != 0 and temperatures[stk[-1]] < t):
            idx = stk.pop()
            ans[idx] = i - idx
        stk.append(i)
    while (len(stk) != 0):
        idx = stk.pop()
        ans[idx] = 0
    return ans