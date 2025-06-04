class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        """
        1st approach: Using string manipulation to add binary numbers
        # This approach is not efficient for large binary strings
        # and is not recommended for production code.
        2nd approach: Using integer conversion for binary addition
        # This approach is more efficient and handles large binary strings well.
        """
        
        # len_a = len(a)
        # len_b = len(b)
        # if len_a < len_b:
        #     a = "0" * (len_b - len_a) + a
        # else:
        #     b = "0" * (len_a - len_b) + b
        # len_ab = max(len_a, len_b)
        # a = a[::-1]
        # b = b[::-1]
        # i = 0
        # sol = ""
        # c = 0
        # while i < len_ab:
        #     s = int(a[i]) + int(b[i]) + c
        #     c = s // 2
        #     s = s % 2
        #     sol = str(s) + sol
        #     i += 1
        # if c == 1:
        #     sol = "1" + sol
        # return sol

        total = int(a, 2) + int(b, 2)
        if total == 0:
            return '0'

        result = ''
        while total > 0:
            rem = total % 2
            result = str(rem) + result
            total //= 2
            
        return result