# LeetCode 3700: Number of ZigZag Arrays II | Matrix Exponentiation + State Compression

# Approach:
# Instead of building arrays directly, we count valid ZigZag sequences using DP
# and accelerate transitions with Matrix Exponentiation.

# 1. Compress values:
#    - Let m = r - l + 1.
#    - Actual values do not matter, only their relative ordering.

# 2. Define DP state:
#    - State k represents the difference rank between two adjacent values.
#    - For a fixed difference state, we track how many valid arrays can end there.

# 3. Build transition matrix:
#    - Matrix A stores valid transitions between states.
#    - A[i][j] = 1 if moving from state j to state i preserves:
#         • adjacent elements are different
#         • no three consecutive elements are strictly increasing
#         • no three consecutive elements are strictly decreasing

# 4. Initialize base vector:
#    - For length 2, each state i contributes i ways.
#    - Store these counts in vector v.

# 5. Fast exponentiation:
#    - We need transitions for (n - 2) additional positions.
#    - Use binary exponentiation on matrix A.
#    - Multiply vector v whenever a bit of exponent is set.

# 6. Compute answer:
#    - Sum all final states.
#    - Multiply by 2 for symmetry of increasing/decreasing directions.
#    - Return result modulo 1e9+7.

# 7. Complexity:
#    - Matrix Size = m × m, where m = r - l + 1 ≤ 75
#    - Time Complexity: O(m³ log n)
#    - Space Complexity: O(m²)


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1

        A = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                if i + j >= m:
                    A[i][j] = 1

        v = [i for i in range(m)]
        e = n - 2

        def mat_mul(X, Y):
            Z = [[0] * m for _ in range(m)]
            for i in range(m):
                Xi = X[i]
                Zi = Z[i]
                for k in range(m):
                    if Xi[k]:
                        a = Xi[k]
                        Yk = Y[k]
                        for j in range(m):
                            Zi[j] = (Zi[j] + a * Yk[j]) % MOD
            return Z

        def mat_vec_mul(M, vec):
            res = [0] * m
            for i in range(m):
                s = 0
                row = M[i]
                for j in range(m):
                    s = (s + row[j] * vec[j]) % MOD
                res[i] = s
            return res

        M = A

        while e:
            if e & 1:
                v = mat_vec_mul(M, v)

            M = mat_mul(M, M)
            e >>= 1

        return (2 * sum(v)) % MOD
