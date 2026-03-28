# ====================================
# Author: Caio Silveira
# Created: 28/03/2026
# ====================================
import math
import sys

# Increase recursion depth to handle larger values of n
sys.setrecursionlimit(10000)


def compute_recursive(n):
    """
    Calculates the value of f(n) using the recurrence relation:
    f(n) = 2f(n-1) + n^2

    Args:
        n (int): The number to be calculated.

    Returns:
        float: The calculated value of f(n).
    """
    if n == 1:
        # Base case
        return 2
    else:
        # Recursive step
        return compute_recursive(n - 1) * 2 + n**2


def compute_closed_form(n):
    """
    Calculates the value of f(n) using the closed-form expression:
    f(n) = 13 * 2^(n-1) - n^2 - 4n - 6

    Args:
        n (int): The number to be calculated.

    Returns:
        float: The calculated value of f(n).
    """
    if n == 1:
        return 2
    else:
        return 13 * math.pow(2, n - 1) - math.pow(n, 2) - 4 * n - 6


# Main execution block
try:
    user_input = int(input("Enter a value for n: "))
    
    if user_input < 1:
        print("n must be greater than or equal to 1")
    else:
        # Calculate results using both methods
        recursive_result = compute_recursive(user_input)
        closed_form_result = compute_closed_form(user_input)
        
        print(f"The value of f({user_input}) [Recursive] is: {recursive_result}")
        print(f"The value of f({user_input}) [Closed Form] is: {closed_form_result}")

except ValueError:
    print("Please enter a valid integer.")