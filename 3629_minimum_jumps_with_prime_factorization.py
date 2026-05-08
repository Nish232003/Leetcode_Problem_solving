# LeetCode: Minimum Jumps with Prime Teleportation | BFS + Prime Mapping

# Approach:
# We treat every index as a node in a graph and use BFS
# to find the minimum jumps required to reach the last index.

# 1. Graph Transitions:
#    From index i, we can:
#       • Move to i - 1
#       • Move to i + 1
#       • Teleport if nums[i] is prime
#
#    If nums[i] is a prime number p,
#    we can jump to every index j where nums[j] % p == 0.

# 2. Prime Factor Preprocessing:
#    - Use SPF (Smallest Prime Factor) sieve
#      for fast prime factorization.
#    - Store indices divisible by each prime factor.

# 3. BFS Traversal:
#    - Start from index 0.
#    - Explore adjacent indices first.
#    - If current value is prime, teleport to all valid indices.
#    - Use visited array to avoid revisiting nodes.

# 4. Optimization:
#    - Each prime teleportation is processed only once
#      using a 'used' set.
#    - Prevents repeated traversal and keeps solution efficient.

# 5. Complexity:
#    - Time Complexity : O(n log M)
#      where M = max(nums)
#    - Space Complexity: O(n + M)


from collections import defaultdict, deque


class Solution(object):
    def minJumps(self, nums):

        n = len(nums)

        if n == 1:
            return 0

        limit = max(nums)

        spf = list(range(limit + 1))

        for i in range(2, int(limit ** 0.5) + 1):

            if spf[i] == i:

                for j in range(i * i, limit + 1, i):

                    if spf[j] == j:
                        spf[j] = i

        factors = defaultdict(list)

        for idx, val in enumerate(nums):

            x = val
            seen = set()

            while x > 1:

                p = spf[x]

                if p not in seen:
                    factors[p].append(idx)
                    seen.add(p)

                x //= p

        q = deque([0])

        vis = [False] * n
        vis[0] = True

        used = set()

        jumps = 0

        while q:

            for _ in range(len(q)):

                i = q.popleft()

                if i == n - 1:
                    return jumps

                if i - 1 >= 0 and not vis[i - 1]:

                    vis[i - 1] = True
                    q.append(i - 1)

                if i + 1 < n and not vis[i + 1]:

                    vis[i + 1] = True
                    q.append(i + 1)

                val = nums[i]

                if val > 1 and spf[val] == val and val not in used:

                    used.add(val)

                    for nxt in factors[val]:

                        if not vis[nxt]:

                            vis[nxt] = True
                            q.append(nxt)

            jumps += 1

        return -1
