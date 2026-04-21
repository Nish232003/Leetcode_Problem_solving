#LC 1722 - Minimize Hamming Distance After Swap Operations

#- Used Union-Find (Disjoint Set) to group swappable indices
#- Treated each connected component independently
#- Applied frequency matching using Counter to minimize mismatches
#- Avoided brute-force swapping by leveraging grouping logic
#- Achieved optimal time complexity of O(n)

from collections import defaultdict, Counter

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        
        parent = list(range(len(source)))

        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        
        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)

        
        result = 0

        for indices in groups.values():
            count = Counter()
            
            
            for i in indices:
                count[source[i]] += 1
            
            
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    result += 1

        return result
