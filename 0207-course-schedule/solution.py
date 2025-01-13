class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pm={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            pm[crs].append(pre)

        v= set()
        def dfs(crs):
            if crs in v:
                return False
            if pm[crs]==[]:
                return True
            v.add(crs)
            for i in pm[crs]:
                if not dfs(i):
                    return False
            v.remove(crs)
            pm[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True                


        
