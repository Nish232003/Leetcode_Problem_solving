# LeetCode 71: Simplify Path | Stack

# Approach:
# We use a stack to simulate directory navigation.
#
# 1. Split the path using '/'.
#
# 2. Process each part:
#    - "" (empty string) → Ignore
#      (caused by multiple slashes)
#
#    - "." → Ignore
#      (current directory)
#
#    - ".." → Move to parent directory
#      (pop from stack if possible)
#
#    - Otherwise:
#      It is a valid directory name,
#      so push it onto the stack.
#
# 3. Construct the canonical path:
#    - Join all directories in the stack
#      using '/'.
#
# 4. If stack becomes empty,
#    return root "/".
#
# 5. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def simplifyPath(self, path):

        stack = []

        for part in path.split("/"):

            # Ignore empty strings and "."
            if part == "" or part == ".":
                continue

            # Move to parent directory
            elif part == "..":
                if stack:
                    stack.pop()

            # Valid directory name
            else:
                stack.append(part)

        return "/" + "/".join(stack)
