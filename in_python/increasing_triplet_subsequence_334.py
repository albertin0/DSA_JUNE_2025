class Solution:
    """ 1st Attempt """
    # def increasingTriplet(self, nums: list[int]) -> bool:
        # smallest_from_left = [0] * len(nums)
        # largest_from_right = [0] * len(nums)

        # if len(nums) < 3:
        #     return False
        
        # smallest_from_left[0] = nums[0]
        # largest_from_right[-1] = nums[-1]


        # i = 1
        # while i < len(nums):
        #     smallest_from_left[i] = min(smallest_from_left[i - 1], nums[i])
        #     largest_from_right[-i - 1] = max(largest_from_right[-i], nums[-i - 1])
        #     i += 1
        
        # for i in range(1, len(nums) - 1):
        #     if smallest_from_left[i - 1] < nums[i] < largest_from_right[i + 1]:
        #         return True
        # return False

    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')
        second = float('inf')


        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        
        return False
    
def test_increasing_triplet():
    s = Solution()
    # 1. Simple increasing triplet
    assert s.increasingTriplet([1, 2, 3, 4, 5]) == True
    # 2. No increasing triplet
    assert s.increasingTriplet([5, 4, 3, 2, 1]) == False
    # 3. Triplet not at start
    assert s.increasingTriplet([2, 1, 5, 0, 4, 6]) == True
    # 4. Only two elements
    assert s.increasingTriplet([1, 2]) == False
    # 5. Triplet with duplicates
    assert s.increasingTriplet([1, 1, 1, 2, 2, 3]) == True
    # 6. Negative numbers
    assert s.increasingTriplet([-3, -2, -1]) == True
    # 7. Triplet with gaps
    assert s.increasingTriplet([10, 1, 2, 3, 0, 4]) == True
    # 8. All elements equal
    assert s.increasingTriplet([2, 2, 2, 2, 2]) == False
    # 9. Triplet at the end
    assert s.increasingTriplet([5, 4, 3, 1, 2, 3]) == True
    # 10. Large input with no triplet
    assert s.increasingTriplet([10]*1000) == False

if __name__ == "__main__":
    try:
        test_increasing_triplet()
    except AssertionError as e:
        print("Assertion failed:", e)
        print("Some test cases failed!")
    else:
        print("All test cases passed!")