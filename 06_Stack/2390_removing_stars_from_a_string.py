class Solution:
    def removeStars(self, s: str) -> str:
        ans = []

        for char in s:
            if char == "*":
                # スタックが空でないことが保証されている問題設定ですが、
                # 実務では if ans: ans.pop() と書くのが安全です
                ans.pop()
            else:
                ans.append(char)
            
        return "".join(ans)