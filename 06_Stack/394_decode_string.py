class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (直前の文字列, 繰り返す回数) を格納するスタック
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                # 数字が2桁以上のケース（例: "12["）に対応
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                # 今までの文字列と回数をスタックに避難させ、リセット
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif char == "]":
                # 避難させていた情報を取り出し、合体させる
                prev_str, num = stack.pop()
                curr_str = prev_str + (curr_str * num)
            else:
                # 通常の文字
                curr_str += char
        
        return curr_str





# --- ローカルテスト用実行ブロック ---
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        "3[a]2[bc]",          # 基本
        "3[a2[c]]",         # 入れ子
        "2[abc]3[cd]ef",      # 複合
        "10[a]",              # 2桁の数字
    ]

    for i, s in enumerate(test_cases):
        print(f"\n--- Test Case {i+1}: input = '{s}' ---")
        result = sol.decodeString(s)
        print(f"Result: '{result}'")