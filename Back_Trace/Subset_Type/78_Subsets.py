'''
78. 子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
子集（幂集）。解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

时间复杂度:o(n * 2^n)
空间复杂度:o(n)

summarize:
1.首先要知道path.copy的用法， 它是将每一次的ans，记录， 互不影响， 但可以到正确的ans
2.而后考虑当前元素是选择还是不选择， 若选择， 将其加到path中， 递归到下一个子集， 直到达到边界条件 i == n 的时候， 而后回溯到上一次
调用， pop尾元素，执行dfs（i + 1） ， 达到边界条件， 枚举子集加到ans中。
3.最后， 又回溯到上一次调用pop尾元素， 执行~， 达到~， 枚举~， 最后结束。

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            dfs(i + 1)
        
        dfs(0)
        return ans


