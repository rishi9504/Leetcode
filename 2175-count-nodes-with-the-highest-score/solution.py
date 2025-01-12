from collections import defaultdict
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        #this was hard, not a med for sure
        #construct tree
        n=len(parents)
        tree = defaultdict(list)
        for child,parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(child)


        ss = [0]*n
        ms = 0
        mc=0
        def dfs(node):
            nonlocal ms,mc
            size=1
            p = 1
            for child in tree[node]:
                cs = dfs(child)
                size+=cs
                p*=cs
            #calculate size of the rest subtree
            rs = n-size
            if rs>0:
                p*=rs
            if p>ms:
                ms = p
                mc=1
            elif p==ms:
                mc+=1
            ss[node]=size
            return size
        dfs(0)
        return mc                            
        
