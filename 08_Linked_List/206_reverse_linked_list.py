class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ガードレール（0個または1個ならそのまま）
        if not head or not head.next:
            return head

        prev = None
        curr = head
        
        # Noneまで行く
        while curr:
            # 1. 未来を確保（next_tempが、currの本来の次をキープ）
            next_temp = curr.next
            
            # 2. 逆転実行（今のサルの紐を、後ろのサルに繋ぎ変える）
            curr.next = prev
            
            # 3. 過去ザルが移動（prevが一歩進む）
            prev = curr
            
            # 4. 現在ザルが移動（currが、確保しておいた未来へジャンプ）
            curr = next_temp
            
        # currがNone（崖の下）に落ちたとき、prevは「元の末尾＝新しい先頭」に立っている
        return prev