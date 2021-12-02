# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def convert(strng, index):
            if strng[index].islower():
                return strng[:index] + strng[index].upper() + strng[index+1:]
            else:
                return strng[:index] + strng[index].lower() + strng[index+1:]

                
        
        hash_map1 = [s]
        hash_map2 = []
        
        for i in range(len(s)):
            if s[i].isalpha():
                for element in hash_map1:
                    hash_map2.append(convert(element, i))
                hash_map1 += hash_map2
                hash_map2 = []
        
        return hash_map1
            
