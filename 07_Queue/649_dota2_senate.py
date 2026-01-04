from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        # 1. 各陣営の「席番号（index）」を管理するキューを用意
        radiant = deque()
        dire = deque()
        
        # 2. enumerateで「場所」と「陣営」を振り分ける
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # 3. 両陣営に議員がいる限り、先頭同士を戦わせる
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # インデックスが小さい方（＝発言順が早い方）が勝利
            if r_idx < d_idx:
                # 勝者は「次の周回（現在の位置 + n）」に並び直す
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
        
        # 4. 生き残った陣営の名前を返す
        return "Radiant" if radiant else "Dire"