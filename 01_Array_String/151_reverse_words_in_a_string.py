class Solution:
    # 自分で考えた方、案1：2ポインタ法（汎用的・アルゴリズムの基礎力を鍛える）
    def reverseWords_v1(self, s: str) -> str:
        split_s = s.split()
        left, right = 0, len(split_s) - 1
        while left < right:
            split_s[left], split_s[right] = split_s[right], split_s[left]
            left += 1
            right -= 1
        return " ".join(split_s)

    # 案2：Pythonic解法（実務・時間の節約・可読性重視）
    def reverseWords(self, s: str) -> str:
        # 最終的に提出するのはこちら。split()の仕様を活かした最短コード。
        return " ".join(s.split()[::-1])