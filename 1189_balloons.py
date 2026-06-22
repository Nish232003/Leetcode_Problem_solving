# LeetCode 1189: Maximum Number of Balloons | Frequency Counting

# Approach:
# Instead of repeatedly forming the word "balloon", we count the frequency
# of characters and determine how many complete instances can be created.

# 1. Count character frequencies:
#    - Use Counter to store occurrences of each character in the string.

# 2. Identify required characters:
#    - "balloon" requires:
#        • b → 1 time
#        • a → 1 time
#        • l → 2 times
#        • o → 2 times
#        • n → 1 time

# 3. Compute the maximum possible instances:
#    - Divide counts of 'l' and 'o' by 2 since each balloon needs two of them.
#    - Take the minimum among all required character counts.

# 4. Return the answer:
#    - The least available requirement determines how many "balloon"s
#      can be formed.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)


from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):

        freq = Counter(text)

        return min(
            freq['b'],
            freq['a'],
            freq['l'] // 2,
            freq['o'] // 2,
            freq['n']
        )
