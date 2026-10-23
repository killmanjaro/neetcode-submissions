class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = {}
        set2 = {}
        for c in s:
            if c in set1:
                set1[c] += 1
            else:
                set1[c] = 0
            
        for c in t:
            if c in set2:
                set2[c] += 1
            else:
                set2[c] = 0

        if set1 == set2:
            return True
        return False






    







        

            