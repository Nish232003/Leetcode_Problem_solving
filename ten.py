# Approach

#1. Read the plaintext message and the encryption key.
#2. Check whether the key is valid.
#   - If the key is less than `0`, print **"INVALID INPUT"** and terminate the program.
#3. Traverse the message character by character.
#4. For each character:
#   - If it is an uppercase letter (`A-Z`), shift it by the given key using modulo `26`.
#   - If it is a lowercase letter (`a-z`), shift it by the given key using modulo `26`.
#   - If it is a digit (`0-9`), shift it by the given key using modulo `10`.
#   - Otherwise (spaces or special characters), keep it unchanged.
#5. Append each transformed character to the encrypted string.
#6. Print the final encrypted message.

message = input()
key = int(input())

if key < 0:
    print("INVALID INPUT")
else:
    result = ""

    for ch in message:

        if ch.isupper():
            new_char = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            result += new_char

        elif ch.islower():
            new_char = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
            result += new_char

        elif ch.isdigit():
            new_char = chr((ord(ch) - ord('0') + key) % 10 + ord('0'))
            result += new_char

        else:
            result += ch

    print("The encrypted Text is:", result)
