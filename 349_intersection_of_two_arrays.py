#Leetcode : 349 Intersection of two arrays
#Approach L:
# We will create set from the first array . Iterate it through second aray and check if number exists in set1. If found add it too the result set and remove it from set1 to avoid duplicates.

def intersection(nums1 , nums2P):
  return list(set(nums1) & set(nums2))
