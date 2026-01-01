class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        n=len(nums)
        write = 0 #0で止めておいて、0以外の数字と入れ替える

        for read in range(n):
            if nums[read] != 0:
                #0の場所と、0以外の場所を交換
                nums[write], nums[read] = nums[read],nums[write]
                #次に0以外を入れる場所を一つ進める
                write += 1 