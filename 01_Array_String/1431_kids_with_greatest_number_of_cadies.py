class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        各子供が extraCandies を受け取った際に最大値になり得るかを判定する。
        
        Time Complexity: O(n) - max()で1回、リスト走査で1回の計2回走査
        Space Complexity: O(n) - 結果格納用のリスト分
        """
        # 閾値を事前に計算し、ループ内の演算を比較のみに最適化
        limit = max(candies) - extraCandies
        return [candy >= limit for candy in candies]