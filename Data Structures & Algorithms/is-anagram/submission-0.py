class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        # for each string, count how many of each letter there are
        # if counts are the same, anagram, else not
        for i in s:
            if i in dict_1:
                dict_1[i] = dict_1[i] + 1
            else:
                dict_1[i] = 1

        for j in t:
            if j in dict_2:
                dict_2[j] = dict_2[j] + 1
            else:
                dict_2[j] = 1
        
        if dict_1.keys() == dict_2.keys():
            for key in dict_1:
                if dict_1[key] != dict_2[key]:
                    return False
        else:
            return False
        return True
        

            