class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        read=0  #読み取り開始位置
        write=0 #書き込み位置
        
        while read < n:
            char = chars[read]
            j = read

            #同じグループがどこまで続くか
            #j < nという境界チェック（Indexerrorを防ぐうえで大切）
            while j<n and chars[j] == char:
                j += 1

            #グループの長さ
            count = j - read

            #現在の文字書き込み
            chars[write] = char
            write += 1

            # 4. 2文字以上連続していれば、数字を1文字ずつ書き込み
            # 10以上の数字も対応できるよう、文字列に変換してループを回す
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            read = j
        # 5. 本体（read）を偵察結果（j）の場所まで一気にワープさせる
        # これにより O(N) の計算量を維持しつつ無限ループを防ぐ
        return write 
