class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        # create dictionary
        # loop through nums
        # add key = target - nums[index], value = index
        # look in dict if num is equal to any key
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dict:
                return [dict[difference], i]
            else:
                dict[nums[i]] = i



        

            



        