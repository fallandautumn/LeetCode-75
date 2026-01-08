# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 【ガードレール】
        # サルが0匹、または1匹（head.nextがNone）なら、並び替える必要がないのでそのまま返す
        if not head or not head.next:
            return head
        
        # 1. サルたちの配置（初期設定）
        # odd（奇数ザル）は1番目、even（偶数ザル）は2番目からスタート
        odd = head
        even = head.next
        # 偶数チームの最初の場所を、後で「合体」させるためにメモ（even_head）しておく
        even_head = even
        
        # 2. 空中ブランコ（バトンパス）の開始
        # 最前線を走る even が「今いる場所」と「一歩先」の両方に手（ノード）がある限り続ける
        while even and even.next:
            # 奇数ザルが、偶数ザルの持っている「次（3番目）」の手を掴む
            odd.next = even.next
            # 奇数ザルがその場所へ移動
            odd = odd.next
            
            # 偶数ザルが、奇数ザルが今移動した場所の「次（4番目）」の手を掴む
            even.next = odd.next
            # 偶数ザルがその場所へ移動
            even = even.next
        
        # 3. 奇数チームと偶数チームのガッチャンコ
        # headから伸びる紐を腰に括り付けたまま進んだ奇数チームの最後に、
        # 温存しておいた偶数チームの先頭を繋げる
        odd.next = even_head
        
        # 玄関（head）から辿れば、新しくリフォームされた奇数・偶数リストが手に入る
        return head