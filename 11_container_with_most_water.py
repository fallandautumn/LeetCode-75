class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0 #面積
        
        while left < right:
            #幅の計算
            width = right - left
            #高さは低い方に引きずられる
            h = min(height[left],height[right])
            #最大面積の更新
            max_area = max(max_area,width*h)
            #低い方のポインタを動かす
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1

        return max_area
  