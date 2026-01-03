class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 1. 集合(Set)を使って検索を高速化 (O(1) lookup)
        vowels = set("aeiou")
        
        # 2. 最初のウィンドウのカウント
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        max_vowels = current_vowels
        
        # 3. 窓をスライドさせる
        for i in range(k, len(s)):
            # 入ってくる文字が母音なら +1
            if s[i] in vowels:
                current_vowels += 1
            # 出ていく文字(i-k)が母音なら -1
            if s[i-k] in vowels:
                current_vowels -= 1
            
            # 最大値を更新 (kに達した時点で早期終了も可能だが、まずは基本に忠実に)
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                
            # もし max_vowels が k に達したら、それ以上大きな値はないので終了(最適化)
            if max_vowels == k:
                return k

        return max_vowels