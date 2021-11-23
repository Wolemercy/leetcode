# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        globalDict = collections.defaultdict(int)
        
        globalDict[0] = 1
        
        for n in nums:
            tempDict = collections.defaultdict(int)
            for k, v in globalDict.items():
                tempDict[k - n] += v
                tempDict[k + n] += v
            globalDict = tempDict
            
        return globalDict[target]
