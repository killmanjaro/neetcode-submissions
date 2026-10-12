class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            # for each element in nums, put into dictionary
            # if key already exists, return false
            # if at the end of iteration, no key showed up twice, 
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]] = "1"
                #print(dict)
        return False
        