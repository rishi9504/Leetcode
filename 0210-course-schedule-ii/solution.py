class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pq={c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            pq[crs].append(pre)
        # a course has 3 possible states:
        # visited-> crs has been added to op
        # visiting-> crs has not been added to op, but added to cycle
        # unvisited-> crs has not been added to op or cycle

        op=[]
        v,c = set(),set()
        def dfs(crs):
            if crs in c:
                return False
            if crs in v:
                return True
            c.add(crs)
            for pre in pq[crs]:
                if dfs(pre)==False:
                    return False
            c.remove(crs)  
            v.add(crs)
            op.append(crs)
            return True
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return op                             

        
