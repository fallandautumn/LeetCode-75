class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # 母音判定を O(1) にするため set を使用（大文字小文字両方）
        vowels = set("aeiouAEIOU")
        # Pythonの文字列はImmutableなためリストに変換
        s_list = list(s)
        
        left, right = 0, len(s) - 1
        
        while left < right:
            # 左から母音を探す
            while left < right and s_list[left] not in vowels:
                left += 1
            # 右から母音を探す
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # 母音同士を交換
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            # ポインタを次に進める
            left += 1
            right -= 1
            
        return "".join(s_list)