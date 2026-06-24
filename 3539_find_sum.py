# LeetCode 3539: Find Sum of Array Product of Magical Sequences | DP + Carry Propagation

# Approach:
# Instead of constructing all possible sequences, we process the indices
# bit by bit and use carry propagation to determine the number of set bits
# in the final binary sum.

# 1. Precompute factorials:
#    - fact[i] stores i!
#    - invfact[i] stores modular inverse of i!
#    - These are used to account for permutations of repeated indices.

# 2. Define DP state:
#    - pos : current index being processed.
#    - used : number of elements selected so far.
#    - carry : carry value coming from lower bits.
#    - bits : number of set bits generated so far.

# 3. Try selecting cnt copies of nums[pos]:
#    - cnt ranges from 0 to (m - used).
#    - total = carry + cnt
#    - Current bit contribution = total & 1
#    - Next carry = total >> 1
#    - Multiply contribution by nums[pos]^cnt and divide by cnt!
#      using invfact[cnt].

# 4. Base case:
#    - After processing all indices, remaining carry contributes
#      carry.bit_count() set bits.
#    - If exactly m elements are chosen and total set bits equal k,
#      return fact[m] to account for all permutations.
#    - Otherwise return 0.

# 5. Complexity:
#    - Time Complexity: O(n * m^3)
#    - Space Complexity: O(n * m^2 * k)


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:

        MOD = 10**9 + 7
        n = len(nums)

        fact = [1] * (m + 1)
        invfact = [1] * (m + 1)

        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact[m] = pow(fact[m], MOD - 2, MOD)

        for i in range(m, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        from functools import cache

        @cache
        def dfs(pos, used, carry, bits):

            if bits > k:
                return 0

            if pos == n:
                bits += carry.bit_count()

                if used == m and bits == k:
                    return fact[m]

                return 0

            ans = 0
            power = 1

            for cnt in range(m - used + 1):

                if cnt > 0:
                    power = power * nums[pos] % MOD

                total = carry + cnt
                new_bits = bits + (total & 1)
                new_carry = total >> 1

                ways = power * invfact[cnt] % MOD

                ans += ways * dfs(
                    pos + 1,
                    used + cnt,
                    new_carry,
                    new_bits
                )

                ans %= MOD

            return ans

        return dfs(0, 0, 0, 0)
