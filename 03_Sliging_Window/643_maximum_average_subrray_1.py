class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #最初の窓の合計
        current_sum = sum(nums[:k])
        max_sum = current_sum
        #窓のスライド
        for i in range(k,len(nums)):
            #窓の右の要素を足し、抜ける左の要素を引く
            current_sum += nums[i]-nums[i-k]
            #合計の状態で保持（毎回割る（平均求める）より効率よい）
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum/k