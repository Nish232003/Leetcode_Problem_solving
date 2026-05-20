# LeetCode 2657: Find the Prefix Common Array of Two Arrays
# Approach: HashMap Frequency Counting

# 1. Initialize:
#    - Use a dictionary 'freq' to track occurrence count of elements.
#    - 'common' stores count of common elements till current index.
#    - 'ans' stores final prefix common array.

# 2. Traverse both arrays together:
#    - Add A[i] frequency.
#    - If frequency becomes 2, it means element appeared in both arrays.
#      So increment common count.
#
#    - Add B[i] frequency.
#    - Again, if frequency becomes 2, increment common count.

# 3. Store result:
#    - Append current common count into answer array.

# 4. Complexity:
#    - Time Complexity: O(n)
#    - Space Complexity: O(n)


class Solution(object):
    def findThePrefixCommonArray(self, A, B):
    
        freq = {}
        common = 0
        ans = []
        
        
        for i in range(len(A)):
            
            
            freq[A[i]] = freq.get(A[i], 0) + 1
            
            if freq[A[i]] == 2:
                common += 1
                
            
            freq[B[i]] = freq.get(B[i], 0) + 1
            
            if freq[B[i]] == 2:
                common += 1
                
            
            ans.append(common)
            
            
        return ans
