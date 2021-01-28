# fib2.py
"""Computes the Fibonacci number for given integer.
   This version works but is inefficient because of
   exponential growth of recursive function calls as 
   n gets larger.
"""
def fib2(n: int) -> int:
    if n < 2: # base case
        return n
    return fib2(n - 2) + fib2(n - 1)

if __name__ == "__main__":
    print(fib2(5))
    print(fib2(50))