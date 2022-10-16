class problem1:

    def rotation(nums, k):
        length = len(nums)
        def helper(nums):
            start = 0
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        helper(nums)
        helper(nums[:k])
        helper(nums[k:])

        return nums







