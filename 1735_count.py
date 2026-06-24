# LeetCode 1735: Count Ways to Make Array With Product | Prime Factorization + Stars and Bars

# Approach:
# Instead of constructing all arrays, we factorize each product and distribute
# the exponents of its prime factors among n positions using combinations.

# 1. Observe:
#    - If:
#          k = p1^e1 * p2^e2 * ... * pt^et
#    - The exponents of each prime are independent.
#    - For a prime with exponent e, we need to distribute e identical objects
#      among n positions.
#    - By Stars and Bars, the number of ways is:
#          C(n + e - 1, e)

# 2. Precompute:
#    - Smallest Prime Factor (SPF) for numbers up to max(k).
#    - Factorials and inverse factorials up to:
#          max(n + total exponent)
#      for efficient combination computation.

# 3. Process each query:
#    - Factorize k using SPF.
#    - For every prime exponent e:
#          multiply answer by C(n + e - 1, e)
#    - Take modulo 10^9 + 7.

# 4. Complexity:
#    - Time Complexity:
#          O(MAX_K log log MAX_K + Q log MAX_K)
#    - Space Complexity:
#          O(MAX_N)


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:

        MOD = 10**9 + 7

        max_n = max(n for n, _ in queries)
        max_k = max(k for _, k in queries)

        spf = list(range(max_k + 1))

        for i in range(2, int(max_k ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_k + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        limit = max_n + 14

        fact = [1] * (limit + 1)
        invfact = [1] * (limit + 1)

        for i in range(1, limit + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact[limit] = pow(fact[limit], MOD - 2, MOD)

        for i in range(limit, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

        answer = []

        for n, k in queries:

            ways = 1

            while k > 1:
                prime = spf[k]
                exponent = 0

                while k % prime == 0:
                    exponent += 1
                    k //= prime

                ways = ways * comb(n + exponent - 1, exponent) % MOD

            answer.append(ways)

        return answer
