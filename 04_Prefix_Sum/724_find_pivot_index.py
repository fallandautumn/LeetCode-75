class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        left_sum = 0
        right_sum = 0

        for i in range(len(nums)):
            #右側＝全体－左側－ピボット点
            right_sum = total_sum - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            #最後にleft_sumをすることで、上の計算の時にnums[i]を二回引くことを避ける
            left_sum+=nums[i]
        
        return -1
