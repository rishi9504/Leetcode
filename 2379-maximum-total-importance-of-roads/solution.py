class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        #submitted for daily challenge, will need to revisit,coded till half but got confused
        res = 0
        cost = 1
        conn = [0] * n
        for road in roads:
            conn[road[0]] += 1
            conn[road[1]] += 1

        conn.sort()
        for con in conn:
            res += con * cost
            cost += 1
        return res
