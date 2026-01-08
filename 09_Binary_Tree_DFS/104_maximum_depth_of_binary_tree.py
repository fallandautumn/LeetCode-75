# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left   # LeetCodeが数式(2n+1)で代入済み
#         self.right = right  # LeetCodeが数式(2n+2)で代入済み

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 【ベースケース】
        # 行き止まり(None)に到達したら、報告値として「0」を返す
        if not root:
            return 0
        
        # 【再帰ステップ：トーナメント開催】
        # 左の部下と右の部下に、それぞれの「最大深さ」を報告させる
        # self. をつけることで、同じクラス内の「数える能力」を再利用
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 【集計：勝利者への加算】
        # 左右の報告値のうち大きい方を採用し、自分自身の階層分(+1)を足して親に返す
        return max(left_depth, right_depth) + 1