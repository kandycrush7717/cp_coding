'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-10-11
    * Time : 4:31 p.m.
    * Question :(https://leetcode.com/problems/robot-bounded-in-circle/)
        On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
        The north direction is the positive direction of the y-axis.
        The south direction is the negative direction of the y-axis.
        The east direction is the positive direction of the x-axis.
        The west direction is the negative direction of the x-axis.
        The robot can receive one of three instructions:
        "G": go straight 1 unit.
        "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
        "R": turn 90 degrees to the right (i.e., clockwise direction).
        The robot performs the instructions given in order, and repeats them forever.
        Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
    * Example :
        Input: instructions = "GGLLGG"
        Output: true
        Explanation: The robot is initially at (0, 0) facing the north direction.
        "G": move one step. Position: (0, 1). Direction: North.
        "G": move one step. Position: (0, 2). Direction: North.
        "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
        "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
        "G": move one step. Position: (0, 1). Direction: South.
        "G": move one step. Position: (0, 0). Direction: South.
        Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
        Based on that, we return true.
'''
import sys
if __name__=='__main__':
    instr=sys.stdin.readline().rstrip('\n')
    (startX,startY)=(endX,endY)=(0,0)
    direction=1
    for i in instr:
        if abs(direction)==1:
            if i=='G':
                endY+=(direction)
            elif i=='L':
                direction*=-3
            elif i=='R':
                direction*=3
        else:
            if i == 'G':
                endX += (direction // 3)
            elif i == 'L':
                direction //= 3
            elif i == 'R':
                direction //= -3
    if (startX, startY) == (endX, endY) or direction != 1:
        sys.stdout.write('True')
    else:
        sys.stdout.write('False')