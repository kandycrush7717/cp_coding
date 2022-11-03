'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2022-11-03
    * Time : 2:46 p.m.
    * Question :(https://leetcode.com/problems/pascals-triangle/)
        Given an integer numRows, return the first numRows of Pascal's triangle.
    * Example :
        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline().rstrip('\n'))
    for _ in range(t):
        numRows=int(sys.stdin.readline().rstrip('\n'))
        ans = [[1], [1, 1]]
        if numRows == 1 or numRows == 2:
            print(ans[:numRows])
        for i in range(3, numRows + 1):
            temp_ans = [1]
            prev = ans[-1]
            i = 0
            j = 1
            lmt = len(prev)
            while (j < lmt):
                temp_ans.append(prev[i] + prev[j])
                i += 1
                j += 1
            temp_ans.append(1)
            ans.append(temp_ans)
        print(ans)

