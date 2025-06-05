class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        len1 = len(word1)
        len2 = len(word2)
        merged = ""
        while i < len1 or i < len2:
            if i < len1:
                merged += word1[i]
            if i < len2:
                merged += word2[i]
            i += 1
        return merged
    
# Example usage:
solution = Solution()
result = solution.mergeAlternately("abc", "pqr")
print(result)  # Output: "apbqcr"

# Example usage:
# solution = Solution()
result = solution.mergeAlternately("ab", "pqrs")
print(result)  # Output: "apbqrs"

# Example usage:
# solution = Solution()
result = solution.mergeAlternately("abcd", "pq")
print(result)  # Output: "apbqcd"

# Example usage:
# solution = Solution()
result = solution.mergeAlternately("", "pqrs")
print(result)  # Output: "pqrs"

# Example usage:
# solution = Solution()
result = solution.mergeAlternately("abc", "")
print(result)  # Output: "abc"

# Example usage:
# solution = Solution()
result = solution.mergeAlternately("", "")
print(result)  # Output: ""

# Example usage:
# solution = Solution()
result = solution.mergeAlternately("a", "b")
print(result)  # Output: "ab"

# Example usage:
# solution = Solution()
result = solution.mergeAlternately("a", "bb")
print(result)  # Output: "abb"

# Example usage:
# solution = Solution()
result = solution.mergeAlternately("abcde", "xyz")
print(result)  # Output: "axbyczde"