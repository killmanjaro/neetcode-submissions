class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # try num 2
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False
