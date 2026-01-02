class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        i=0 #見つけたい目標
        j=0 #探索対象

        #初めからsに何も入っていないときに終了
        if len_s == 0:
            return True

        while j < len_t and i < len_s:
            
            if s[i] == t[j]:
                i += 1

            j+=1

        return i == len_s