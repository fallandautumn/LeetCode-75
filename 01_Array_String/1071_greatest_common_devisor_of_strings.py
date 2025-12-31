import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        
        gcd_length = math.gcd(len(str1),len(str2))
        return str1[:gcd_length]        






if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("ABCABC","ABC"),
        ("ABABAB","ABAB"),
        ("LEET","CODE")
    ]

    for s1,s2 in test_cases:
        result = sol.gcdOfStrings(s1,s2)
        print(f"Input: str1='{s1}', str2='{s2}' -> Result: '{result}'")