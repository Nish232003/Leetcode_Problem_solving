# LeetCode 192: Word Frequency | Unix Pipes

# Approach:
# 1. Convert spaces into new lines so each word appears on a separate line.
# 2. Sort all words together.
# 3. Count occurrences of each word using uniq -c.
# 4. Sort by frequency in descending order.
# 5. Print word followed by frequency.
#
# Example:
# Input:
# the day is sunny the the
# the sunny is is
#
# After processing:
# the 4
# is 3
# sunny 2
# day 1
#
# Complexity:
#    - Time Complexity: O(n log n)
#    - Space Complexity: O(n)

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'
