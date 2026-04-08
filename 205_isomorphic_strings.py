#Leetcode : 205 : Isomorphic strings
#Approach:
# Two strings are isomorphic if we can replace characters in s to get t where each character maps to exactly one character and no two cgaracters map to the same character.

def is_isomorphic(s: str , t: str) :
  if len(s) != len(t):
    return False
  char_mapping_map = {}
  for i in range(len(s)):
    original = s[i]
    replacement = t[i]
    if original not in char_mapping_map:
      if replacement not in char_mapping_map.values():
        char_mapping_map[original] = replacement
      else:
        return False
    else:
      mapped_character = char_mapping_map[original]
      if mapped_character != replacement:
        return False
    return True
