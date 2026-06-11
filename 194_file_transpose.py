# LeetCode 194: Transpose File | AWK

# Approach:
# 1. Read the file row by row using awk.
#
# 2. Store each field in a matrix:
#       a[row,column] = value
#
# 3. Track:
#       NR = number of rows
#       NF = number of columns
#
# 4. After reading the file:
#       - Iterate column by column.
#       - Print all values from top to bottom.
#
# 5. This effectively converts rows into columns.
#
# Example:
#
# Input:
# name age
# alice 21
# ryan 30
#
# Matrix:
# name  age
# alice 21
# ryan  30
#
# Output:
# name alice ryan
# age 21 30
#
# Complexity:
#    - Time Complexity: O(m × n)
#    - Space Complexity: O(m × n)

awk '
{
    for (i = 1; i <= NF; i++)
        a[NR,i] = $i
}
END {
    for (i = 1; i <= NF; i++) {
        for (j = 1; j <= NR; j++) {
            printf a[j,i]
            if (j < NR)
                printf " "
        }
        printf "\n"
    }
}' file.txt
