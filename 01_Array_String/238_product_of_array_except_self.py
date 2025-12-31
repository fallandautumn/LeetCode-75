class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        
        # 1. 左側からの累積積を計算して ans に格納する
        # ans[i] は nums[0] から nums[i-1] までの積になる
        left_product = 1
        for i in range(n):
            ans[i] = left_product
            left_product *= nums[i]
            
        # 2. 右側からの累積積を「その場で」掛け合わせていく
        # 別途配列を作らず変数で保持することで空間計算量を節約（実務上の工夫）
        right_product = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]
            
        return ans