# Approach:

# Instead of checking each alphabet manually, we use a set to store only unique characters.

# 1. Read the input string.

# 2. Convert the string into a set:
# - A set automatically removes duplicate characters.
# - Only unique letters remain.

# 3. Check the size of the set:
# - If the size is 26, all lowercase English letters are present.
# - Otherwise, at least one letter is missing.

# 4. Print the result:
# - Print "True" if all 26 letters are present.
# - Otherwise, print "False".

# 5. Complexity:
# - Time Complexity: O(n)
# - Space Complexity: O(1)

s = input()

letters = set(s)

if len(letters) == 26:
    print("True")
else:
    print("False")
