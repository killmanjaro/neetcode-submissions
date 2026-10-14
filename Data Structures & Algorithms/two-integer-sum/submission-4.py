class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


        # first attempt
        '''
        # create dictionary
        # loop through nums
        # add key = target - nums[index], value = index
        # look in dict if num is equal to any key
        dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dict:
                return [dict[difference], i]
            else:
                dict[nums[i]] = i
        '''

        # brute force (O(n^2))
        '''
        for i in range(len(nums)):
            for j in range(len(nums)):
                difference = target - nums[j]
                if nums[i] == difference:
                    return [i, j]
        '''

        # hashmap
        prevMap = {} # val: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i




        

            



        