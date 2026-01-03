class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 0. 長さが違えば絶対に不可能
        if len(word1) != len(word2):
            return False

        word1_dict = {}
        word2_dict = {}

        # 1. 各文字の出現回数をカウント
        for char in word1:
            word1_dict[char] = word1_dict.get(char, 0) + 1
        for char in word2:
            word2_dict[char] = word2_dict.get(char, 0) + 1

        # 2. 条件1: 使われている文字の種類（keys）が一致しているか
        # 集合(set)にして比較するのが最も効率的
        if set(word1_dict.keys()) != set(word2_dict.keys()):
            return False

        # 3. 条件2: 出現回数（values）の分布が一致しているか
        # ソートしたリスト同士を比較することで、分布の一致を確認できる(valuesは順番が保証されていないためsort必要)
        return sorted(word1_dict.values()) == sorted(word2_dict.values())
