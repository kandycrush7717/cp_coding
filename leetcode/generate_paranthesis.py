'''
    * Author : VenkataPraveen Kandimalla
    * Date : 2023-02-12
    * Time : 6:20 p.m.
    * Question :(https://leetcode.com/problems/generate-parentheses/)
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    * Example :
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
'''
class Solution:
    def validParanthesis(self, res, opened, closed, eachTotal, ans):
        if opened == closed == eachTotal:
            ans.append(res)
            return
        if opened < eachTotal:
            self.validParanthesis(res + '(', opened + 1, closed, eachTotal, ans)
        if closed < opened:
            self.validParanthesis(res + ')', opened, closed + 1, eachTotal, ans)

    def generateParenthesis(self, n: int) -> List[str]:
        res = ""
        ans = []
        self.validParanthesis(res, 0, 0, n, ans)
        return ans
