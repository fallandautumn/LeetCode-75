class Solution:
    """
    2つの文字列を交互にマージする。
    Time Complexity: O(n + m) - 各文字を一回ずつ走査
    Space Complexity: O(n + m) - 結果格納用のリストに全文字を保持
    """
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 文字列結合のO(N^2)化を避けるため、ミュータブルなリストをバッファとして使用
        res: list[str] = []
        
        # 独立したポインタにより、長さの異なる入力にも柔軟に対応
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)

        # いずれかの文字列に未処理の文字がある限り継続
        while i < n1 or j < n2:
            if i < n1:
                res.append(word1[i])
                i += 1
            if j < n2:
                res.append(word2[j])
                j += 1

        # 最後に一括結合することで、メモリ確保の回数を最小限に抑える(O(N))
        return "".join(res)