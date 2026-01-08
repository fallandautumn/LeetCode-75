class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. 中間地点の特定（ウサギとカメ）
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. 後半部分の反転（3サルの奥義）
        prev = None
        curr = slow
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        # 3. ツイン和の計算
        left = head
        right = prev # prevは反転後の後半の先頭（元の末尾）
        maxi = 0
        
        # なぜ判定が right (prev) なのか？
        # 後半チーム（right）が None になるまで歩けば、
        # 前半チーム（left）もちょうど半分まで進み、全ペアの計算が終わるから。
        while right: # ここを right に修正（prevでも良いが、更新している変数を使う）
            total = left.val + right.val
            maxi = max(maxi, total)
            left = left.next
            right = right.next # ここで right が None に向かって進む
        
        return maxi