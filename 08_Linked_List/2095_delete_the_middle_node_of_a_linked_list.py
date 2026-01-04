# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 境界条件：ノードが1つしかない場合
        # 紐を結び変える相手がいないので、リストそのものを空（None）にする
        if not head or not head.next:
            return None
        
        # 2. 初期位置の設定
        # カメ(slow)を「真ん中の1つ手前」で止めたいので、ウサギ(fast)を2歩先行させる
        slow = head
        fast = head.next.next
        
        # 3. ウサギとカメの追跡
        # 「fastの中身があるか」かつ「その隣に道があるか」を毎回確認する（安全装置）
        while fast and fast.next:
            slow = slow.next      # カメは1歩進む（紐を1つ辿る）
            fast = fast.next.next # ウサギは2歩進む（紐を2つ辿る）
            
        # 4. 運命の「紐の結び変え」
        # 
        # slowは今、真ん中の直前にいる。
        # slow.next（真ん中）を飛ばして、slow.next.next（真ん中の次）に直接紐を結ぶ。
        slow.next = slow.next.next
        
        # 5. 改造し終わったリストの先頭を返す
        return head