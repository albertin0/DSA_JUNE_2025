# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        while str2 and str1.startswith(str2):
            str1 = str1[len(str2):]
            return self.gcdOfStrings(str2, str1)
        
        return str1 if not str2 else ""
    
# Example usage:
if __name__ == "__main__" :
    sol = Solution()
    # // write test cases using assert statements
    try:
    # print(sol.gcdOfStrings("ABCABC", "ABC"))
    # print(sol.gcdOfStrings("ABABAB", "ABAB"))
    # print(sol.gcdOfStrings("LEET", "CODE"))
    # print(sol.gcdOfStrings("A", "A"))
    # print(sol.gcdOfStrings("A", "B"))
    # print(sol.gcdOfStrings("ABABAB", "ABAB"))
    # print(sol.gcdOfStrings("ABABAB", "AB"))
    # print(sol.gcdOfStrings("ABABAB", "A"))
    # print(sol.gcdOfStrings("ABABAB", "B"))
    # print(sol.gcdOfStrings("ABABAB", "ABABAB"))
    # print(sol.gcdOfStrings("ABABAB", "ABABABA"))
    # print(sol.gcdOfStrings("ABABAB", "ABABABA"))
    # print(sol.gcdOfStrings("ABABAB", "ABABABAB"))
    # print(sol.gcdOfStrings("ABABAB", "ABABABABAB"))
    # print(sol.gcdOfStrings("ABABAB", "ABABABABABAB"))
        assert sol.gcdOfStrings("ABCABC", "ABC") == "ABC"
        assert sol.gcdOfStrings("ABABAB", "ABAB") == "AB"
        assert sol.gcdOfStrings("LEET", "CODE") == ""
        assert sol.gcdOfStrings("A", "A") == "A"
        assert sol.gcdOfStrings("A", "B") == ""
        
        assert sol.gcdOfStrings("ABABAB", "ABAB") == "AB"
        assert sol.gcdOfStrings("ABABAB", "AB") == "AB"
        assert sol.gcdOfStrings("ABABAB", "A") == ""
        assert sol.gcdOfStrings("ABABAB", "B") == ""
        assert sol.gcdOfStrings("ABABAB", "ABABAB") == "ABABAB"
        assert sol.gcdOfStrings("ABABAB", "ABABABA") == ""
    except AssertionError as e:
        print("Assertion failed:", e.with_traceback)
        print("Some test cases failed!")
    else:
        print("All test cases passed!")