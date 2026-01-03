class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        # 差集合（AにあってBにないもの）をリスト化して返す
        return [list(set1-set2),list(set2-set1)]

#以下明示的な書き方

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        
        # res1: set1の要素のうち、set2に含まれないものを抽出
        res1 = [x for x in set1 if x not in set2]
        # res2: set2の要素のうち、set1に含まれないものを抽出
        res2 = [x for x in set2 if x not in set1]
        
        return [res1, res2]