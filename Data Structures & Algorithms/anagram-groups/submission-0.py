class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # make a hasmap
        # key is count, value is words corresponding
        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            # at most 26 unique charas
            count = [0] * 26 # a ... z
            for c in s:
                # we want to map 0 to a, 26 to z
                # so we take the ascii val of our char - ascii val of a
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        return list(res.values())



 

            
        