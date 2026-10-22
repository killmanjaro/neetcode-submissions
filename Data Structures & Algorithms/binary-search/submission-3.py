class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # first attempt
        '''
        def helper (low, high):
            if low > high:
                return -1
            mid = (high + low) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                print("target > nums[mid]")
                return helper(mid + 1, high)
            elif target < nums[mid]:
                print("target < nums[mid]")
                return helper(low, mid - 1)
            else:
                return -1
        return helper(0, len(nums) - 1)
        '''

        # two pointers, one on left and one at right
        # compare midpoint to target
        # shift pointers
        l, r = 0, len(nums) -1

        while l <= r:
            m = (l + r) // 2
            # check leftmost vals
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
        


        