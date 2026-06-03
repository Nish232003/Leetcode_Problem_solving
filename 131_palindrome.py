# LeetCode 131: Palindrome Partitioning | Backtracking

# Approach:
# We need to generate all possible partitions such that
# every substring in the partition is a palindrome.
#
# 1. Use backtracking starting from index 0.
#
# 2. At each position:
#    - Try every possible substring s[start:end+1].
#    - Check if the substring is a palindrome.
#
# 3. If it is a palindrome:
#    - Add it to the current partition.
#    - Recur for the remaining string.
#    - Backtrack by removing the substring.
#
# 4. When start reaches the end of the string:
#    - A valid partition is formed.
#    - Add a copy of the partition to the result.
#
# Example:
# s = "aab"
#
# Partitions explored:
# "a" -> "a" -> "b"    => ["a","a","b"]
# "aa" -> "b"          => ["aa","b"]
#
# Result:
# [["a","a","b"],["aa","b"]]
#
# Complexity:
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)   (recursion stack)


class Solution(object):
    def partition(self, s):
        result = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])

        return result
