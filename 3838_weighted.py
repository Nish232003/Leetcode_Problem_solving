# LeetCode 3838: Weighted Word Mapping | Simulation

# Approach:
# For each word:
#
# 1. Compute its weight:
#    - Sum the weights of all characters.
#
# 2. Take modulo 26:
#    - rem = word_weight % 26
#
# 3. Map using reverse alphabetical order:
#    - 0 -> 'z'
#    - 1 -> 'y'
#    - ...
#    - 25 -> 'a'
#    - Character = chr(ord('z') - rem)
#
# 4. Append the mapped character to the answer.
#
# 5. Return the final concatenated string.
#
# 6. Complexity:
#    - Time Complexity: O(total characters in all words)
#    - Space Complexity: O(words.length)


class Solution:
    def stringMap(self, words, weights):
        ans = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            ans.append(chr(ord('z') - (total % 26)))

        return "".join(ans)
