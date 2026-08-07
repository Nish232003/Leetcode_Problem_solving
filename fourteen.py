#Approach:
# Read the input string : Store the complete paragraph as a string.
# Split the paragraph : Use the split(",") function to divide the paragraph into individual sentences.
# Find the longest sentence : Traverse each sentence. Calculate its length using len(). Keep updating the maximum length whenever a longer sentence is found.
# Print the result : Display the length of the longest sentence.

story = input()
sentences = story.split(",")
max_length = 0
for sentence in sentences:
  length = len(sentence)
  if length > max_length:
    max_length = length
print(max_length)
