class Problem1(object):

    def rotation(self, nums, k):
        length = len(nums)
        def helper(nums):
            start = 0
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return nums

        helper(nums)
        helper(nums[:k])
        helper(nums[k:])

        return helper(nums[:k])+helper(nums[k:])


def main():
    nums = [1,2,3,4,5,6,7]
    k = 3
    problem1 = Problem1()
    print(problem1.rotation(nums, k))


main()




