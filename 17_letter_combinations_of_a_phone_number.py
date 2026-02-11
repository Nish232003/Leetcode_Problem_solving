#Add an efficient single-pass solution for the Two Sum problem using a hash map.
#The approach stores each number with its index while traversing the array and
#checks if the required complement (target − current value) already exists.

#Time Complexity: O(n)
#Space Complexity: O(n)

lass Solution(object):
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
            
            if index == len(digits):
                result.append("".join(path))
                return
            
            
            letters = phone_map[digits[index]]
            for ch in letters:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()  

        backtrack(0, [])
        return result
