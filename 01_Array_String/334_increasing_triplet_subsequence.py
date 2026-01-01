class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # 左からの累積最小
        left_min = [0] * n
        left_min[0] = nums[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], nums[i])
        
        # 右からの累積最大
        right_max = [0] * n
        right_max[n-1] = nums[n-1]
        for j in range(n-2, -1, -1):
            right_max[j] = max(right_max[j+1], nums[j])

        # 判定（kの範囲は、前後に要素がある1からn-2まででOK）
        for k in range(1, n - 1):
            # 「左側の最小」が自分より小さく、かつ「右側の最大」が自分より大きいか
            if left_min[k-1] < nums[k] < right_max[k+1]:
                return True # 見つかった瞬間に終了
        
        # 全てのループが終わっても見つからなければ、ここで初めてFalseを返す
        return False
    
#最適解
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 無限を入れることで、Firstの最初の要素には必ず値が入る。
        # secondはfirst より後ろにあり、かつ first より大きい値の中で最小のものを保持
        first = second = float('inf')
        for n in nums:
            if n <= first: first = n
            elif n <= second: second = n
            else: return True
        return False