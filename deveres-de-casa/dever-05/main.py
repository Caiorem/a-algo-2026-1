# ====================================
# Author: Caio Silveira
# Created: 05/04/2026
# ====================================
import math

def analyze_complexity(a, b, k, p):
    """
    Complexity analyzer for the Master Theorem.

    This function prints the input parameters, the expression for f(n), 
    and the result of the asymptotic complexity analysis.

    The analysis is based on the Master Theorem, which defines the complexity 
    of a recursive algorithm as T(n) = aT(n/b) + f(n), where a > 0 and b > 1 
    are constants, f(n) is a function roughly n^k * log^p(n), and 
    n^(log_b a) is the watershed/dominating term.

    Parameters:
        a (float): The number of subproblems.
        b (float): The factor by which the problem size is reduced.
        k (float): The exponent of n in f(n).
        p (float): The exponent of log(n) in f(n).

    Returns:
        None
    """
    log_b_a = math.log(a, b)
    epsilon = 1e-9

    print(f"\nInput: a={a}, b={b}, k={k}, p={p}")
    print(f"f(n) = n^{k}" + (f" * log^{p}(n)" if p != 0 else ""))
    print(f"n^(log_{b} {a}) = n^{log_b_a:.4f}")
    print("-" * 45)

    # Comparison between the work done in subproblems vs.