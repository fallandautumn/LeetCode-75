class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        # 【設計思想】
        # 「最大k個の0を1に置換できる」＝「窓の中に0がk個まで含まれても良い」と解釈。
        # 窓の中に0がk個以下の間は、その窓全体を「連続する1」とみなすことができる。
        
        for right in range(len(nums)):
            # 1. 右端を広げ、新しく入った要素が 0 ならカウント
            if nums[right] == 0:
                zero_count += 1
            
            # 2. 0の数が許容範囲(k)を超えた場合、左端を縮小させて0を追い出す
            # このループにより、ウィンドウ内は常に「0がk個以下」という条件が保たれる
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # 3. 条件を満たした状態での窓の幅を計算し、最大値を更新
            # 置換後の「連続する1」の長さは、現在の窓の幅そのもの (right - left + 1)
            max_len = max(max_len, right - left + 1)
            
        return max_len