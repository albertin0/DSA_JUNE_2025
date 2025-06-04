class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        cur_num = None
        cur_count = 0
        last = len(nums) - 1
        i = 0
        while i < len(nums) and i <= last:
            num = nums[i]
            if num == cur_num:
                if cur_count < 2:
                    cur_count+=1
                    i += 1
                else:
                    for j in range(i,last):
                        nums[j] = nums[j+1]
                    last -= 1
                    i = i
            else:
                cur_num = num
                cur_count = 1
                i += 1
        return last + 1

s = Solution()

lst = [1,1,1,2,2,2,3,3,3,4,5]

print(s.remove_duplicates(lst))

print(lst)