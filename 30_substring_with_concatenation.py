# LeetCode 30: Substring with Concatenation of All Words
# Sliding Window + HashMap Approach

# Approach:
# Instead of checking every possible substring separately,
# we use a sliding window with word-frequency tracking.

# 1. Handle edge cases:
#    - If string 's' or array 'words' is empty, return [].
#    - If total concatenated length exceeds len(s), return [].

# 2. Initialize:
#    - Store frequency of each word in 'required'.
#    - Each word has same length -> use fixed-size chunks.
#    - Use multiple sliding windows starting from:
#         0 to word_length - 1

# 3. Sliding Window Traversal:
#    - Extract words of fixed size.
#    - Track current window frequencies using hashmap.
#    - If frequency exceeds requirement:
#         shrink window from left.
#    - If valid count matches total words:
#         store starting index.

# 4. Invalid Word Handling:
#    - Clear current window.
#    - Reset counters and move left pointer.

# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(k)
#      where k = number of unique words


class Solution(object):
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        if total_len > len(s):
            return []

        required = {}

        for word in words:
            required[word] = required.get(word, 0) + 1

        result = []

        for start in range(word_len):

            left = start
            count = 0
            current = {}

            for right in range(start, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                if word in required:

                    current[word] = current.get(word, 0) + 1
                    count += 1

                    while current[word] > required[word]:

                        left_word = s[left:left + word_len]
                        current[left_word] -= 1

                        left += word_len
                        count -= 1

                    if count == total_words:

                        result.append(left)

                        left_word = s[left:left + word_len]
                        current[left_word] -= 1

                        left += word_len
                        count -= 1

                else:

                    current.clear()
                    count = 0
                    left = right + word_len

        return result
