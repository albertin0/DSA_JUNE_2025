from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        
        for src, dst in tickets:
            # adj[src].append(dst)
            heapq.heappush(adj[src], dst)
            
        # Sort children to visit lexically smaller destinations first
        # for src in adj:
            # adj[src].sort()
            
        res = []
        def dfs(src):
            res.append(src)
            while adj[src]:
                dst = heapq.heappop(adj[src])
                dfs(dst)
            
        dfs("JFK")
        return res