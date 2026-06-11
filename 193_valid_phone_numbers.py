# LeetCode 193: Valid Phone Numbers | Regular Expressions

# Approach:
# 1. Use grep with Extended Regular Expressions (-E).
#
# 2. Match either of the valid formats:
#
#    a) xxx-xxx-xxxx
#       - 3 digits
#       - hyphen
#       - 3 digits
#       - hyphen
#       - 4 digits
#
#    b) (xxx) xxx-xxxx
#       - opening parenthesis
#       - 3 digits
#       - closing parenthesis
#       - space
#       - 3 digits
#       - hyphen
#       - 4 digits
#
# 3. Use ^ and $ to ensure the entire line matches.
#
# Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(1)

grep -E '^([0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\)\ [0-9]{3}-[0-9]{4})$' file.txt
