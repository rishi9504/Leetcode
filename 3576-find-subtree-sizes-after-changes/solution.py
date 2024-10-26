from collections import defaultdict,deque
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)
        
        tree = defaultdict(list)
        for child in range(1, n):
            tree[parent[child]].append(child)
        
        new_parent = parent[:]
        
        closest_ancestor = defaultdict(list)
        
        def dfs(node):
            char = s[node]
            if closest_ancestor[char]:
                new_parent[node] = closest_ancestor[char][-1]
            
            closest_ancestor[char].append(node)
            
            for child in tree[node]:
                dfs(child)
            
            closest_ancestor[char].pop()
        
        dfs(0)
        
        new_tree = defaultdict(list)
        for child in range(1, n):
            new_tree[new_parent[child]].append(child)
        
        subtree_size = [0] * n
        
        def calculate_size(node):
            size = 1 
            for child in new_tree[node]:
                size += calculate_size(child)
            subtree_size[node] = size
            return size
        
        calculate_size(0)
        
        return subtree_size
