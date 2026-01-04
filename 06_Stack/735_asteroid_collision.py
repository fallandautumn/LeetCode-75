class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = [] # スタックとして使用

        for new in asteroids:
            is_alive = True
            
            # 衝突条件：スタックのトップが右向き(+) かつ 新しい小惑星が左向き(-)
            while is_alive and ans and (ans[-1] > 0 and new < 0):
                if abs(new) > ans[-1]:
                    # 1. 自分の方が大きい：相手を破壊して継続
                    ans.pop()
                    continue 
                elif abs(new) == ans[-1]:
                    # 2. 相打ち：相手を破壊し、自分も消滅
                    ans.pop()
                    is_alive = False
                else:
                    # 3. 自分の方が小さい：自分が消滅
                    is_alive = False
                
                # 相打ち、または敗北した場合は while を抜ける
                break
            
            # 誰にも破壊されずに生き残った場合のみ、スタックに追加
            if is_alive:
                ans.append(new)
                
        return ans