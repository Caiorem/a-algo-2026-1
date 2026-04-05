# ====================================
# Title: Palindrome
# Author: Caio Silveira
# Created: 23/03/2026
# ====================================

def is_palindrome(sequence):
    """
    Checks if a sequence (string or list) is a palindrome.

    Args:
        sequence (list|str): The sequence to be checked.

    Returns:
        str: "Is a Palindrome" or "Is NOT a Palindrome".
    """
    # Base case: if the sequence has 0 or 1 elements, it is a palindrome
    if len(sequence) <= 1:
        return "Is a Palindrome"
    else:
        # Recursive step: check if first and last elements match
        if sequence[0] == sequence[-1]:
            # Recurse with the middle part of the sequence
            return is_palindrome(sequence[1:-1])
        else:
            return "Is NOT a Palindrome"


# Test cases
print(is_palindrome([0, 1, 2, 3, 2, 1, 0]))
print(is_palindrome(["a", "b", "b", "a"]))
print(is_palindrome(["a", "b", "c", "b", "a"]))
print(is_palindrome(["a", "b", "c", "f", "b", "a"]))