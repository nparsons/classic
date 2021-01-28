# fib1.py
"""Computes the Fibonacci value for a given integer.  
   Produces infinite recursion since there is no base case.
"""
def fib1(n: int) -> int:
    return fib1(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(fib1(5))