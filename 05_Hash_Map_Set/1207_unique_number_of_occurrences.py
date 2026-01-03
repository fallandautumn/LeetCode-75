class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 1. 各要素の出現回数を数える（ハッシュマップ）
        counts_dict = {}
        for num in arr:
            if num in counts_dict:
                counts_dict[num] += 1
            else:
                counts_dict[num] = 1
        
        # 2. 出現回数（values）だけを抽出する
        # 例: {1: 3, 2: 2, 3: 1} -> [3, 2, 1]
        occurrences = counts_dict.values()
        
        # 3. 回数に重複がないか、集合(Set)を使って判定する
        # setに入れると重複が消えるため、長さが変わらなければ「すべてユニーク」
        return len(occurrences) == len(set(occurrences))
    

#実務でのプロの書き方
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Counterが一瞬で {数字: 回数} の辞書を作ってくれる
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))