# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #initialize hash set to keep a list of the courses and their prerequisites
        
        courseSet = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            courseSet[crs].append(preq)
        
        #initialize visitSet to keep track of visited courses
        visitSet = set()
        
        
        #write recursive dfs function to traverse the graph
        def dfs(crs):
            if crs in visitSet:
                return False
            
            if courseSet[crs] == []:
                return True
            
            visitSet.add(crs)
            
            for preq in courseSet[crs]:
                if not dfs(preq):
                    return False
            visitSet.remove(crs)
            courseSet[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
