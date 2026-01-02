class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #sortする（最大のポイント）
        nums.sort()
        left = 0
        right = len(nums)-1
        count = 0
        #左右からパトロールする
        while left < right:
            total = nums[left]+nums[right]
            if total == k:
                count+=1
                left +=1
                right -=1
            #合計より小さいので、より大きい数字を求めて左を右へ。
            elif total < k:
                left += 1
            else:
                right -= 1
        return count

