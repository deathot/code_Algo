'''
198. 打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

Tc:o(n)
Sc:o(n)

Summarize:
1.从回溯中进行思考， 当前操作是什么？ 子问题是什么？
2.所以， 对于此题， 自底向上思考， 递归到第i个， 那么下一个子问题就是， 选或不选， 分别是i-1， i-2， 最终返回最大的即可
3.优化空间， 则可添加一个cache来记录已经计算过的第i次递归

'''
#法1
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        def dfs(i):
            if i < 0:
                return 0

            if cache[i] != -1:
                return cache[i]
                
            res = max(dfs(i - 1), dfs(i - 2) + nums[i])
            cache[i] = res
            return res

        return dfs(n-1)
    
#法2 Sc:o(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f0 = f1 = 0
        for i, x in enumerate(nums):
            new_f = max(f1, f0 + x)
            f0 = f1
            f1 = new_f

        return f1
        