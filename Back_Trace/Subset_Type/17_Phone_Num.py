'''
17. 电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

时间复杂度o()
空间复杂度o()

总结:
1.首先考虑当前操作是什么， 而后考虑子集是什么， 最后考虑下一个子集是什么。
2.边界条件就是当path路径的长度和给定的digits相等后就回溯到下一个

'''
MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        
        ans = []
        path = [''] * n

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i + 1)
        dfs(0)
        return ans