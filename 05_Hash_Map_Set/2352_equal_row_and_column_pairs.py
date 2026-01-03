class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = {}
        
        # 1. 各行を「名前(キー)」にして回数を数える
        for row in grid:
            row_key = tuple(row) # リストはキーにできないのでタプル化
            row_counts[row_key] = row_counts.get(row_key, 0) + 1
            
        ans = 0
        n = len(grid)
        
        # 2. 各列を取り出し、その「名前」が辞書にあるか引く
        for j in range(n):
            # 列をタプルとして抽出
            col_key = tuple(grid[i][j] for i in range(n))
            
            # もし「列と同じ名前の行」が辞書にあれば、その出現回数を足す
            if col_key in row_counts:
                ans += row_counts[col_key]
                
        return ans