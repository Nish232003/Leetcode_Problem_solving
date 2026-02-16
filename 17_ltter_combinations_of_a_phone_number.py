# Add an efficient backtracking solution for Letter Combinations of a Phone Number.
# The approach maps each digit to its corresponding letters and builds
# all possible combinations using recursion.

# Time Complexity: O(4^n)
# Space Complexity: O(n)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            # If current combination length equals digits length
            if index == len(digits):
                result.append(path)
                return

            possible_letters = phone_map[digits[index]]

            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result


# Example run
if __name__ == "__main__":
    digits = "23"
    sol = Solution()
    print(sol.letterCombinations(digits))
    # Output: ['ad','ae','af','bd','be','bf','cd','ce','cf']
