class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            # for each element in nums, put into dictionary
            # if key already exists, return false
            # if at the end of iteration, no key showed up twice, 
            if num in hashset:
                return True
            else:
                hashset.add(num)
                #print(dict)
        return False
        