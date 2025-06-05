class Solution:
    def reverseWords(self, s: str) -> str:
        # Strip leading and trailing whitespace
        s = s.strip()
        # Split the string into words
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join the reversed words with a single space
        return ' '.join(words)
    
# Explaination:
# The function reverseWords takes a string s as input, removes leading and trailing whitespace,
# splits the string into words, reverses the order of the words, 
# and then joins them back together with a single space.
# The function returns the resulting string with the words in reverse order.

# Explaination of s.split():
# The split() method splits a string into a list where each word is a list item.
# If no arguments are provided, it splits by whitespace and removes extra spaces.
# The reverse() method reverses the elements of the list in place.



# Example usage:
solution = Solution()
result = solution.reverseWords("  the sky is blue  ")
print(result)  # Output: "blue is sky the"

# Example usage:
result = solution.reverseWords("  hello world  ")
print(result)  # Output: "world hello"

# Example usage:
result = solution.reverseWords("a good   example")
print(result)  # Output: "example good a"

# Example usage:
result = solution.reverseWords("  Bob    Loves  Alice   ")
print(result)  # Output: "Alice Loves Bob"

# Example usage:
result = solution.reverseWords("Alice does not even like bob")
print(result)  # Output: "bob like even not does Alice"

# Example usage:
result = solution.reverseWords("  ")
print(result)  # Output: ""