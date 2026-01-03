# %%
def isodd(x):
    "this function checks if a number is odd by looking the last binary digit."
    return x & 1 == 1


# %%
def gcd(a, b):
    "This function calculates the Greatest Common Divisor of given numbers in a modern way."
    while b:
        a, b = b, a % b
    return a


# %%
def fibonacci(a=0, b=1):
    """
    This generates the fibonacci numbers.
    Optionally you can specify initial values of a and b.
    """
    while True:
        yield a
        a, b = b, a + b


# %%
def factorial(n):
    "This function calculates the factorial of a number."
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    m = 1
    for i in range(2, n + 1):
        m *= i
    return m


# %%
def isprime(n):
    """This function checks if a number is prime."""
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


# %%
def compare(f1, f2, xs):
    "This function compares two functions f1 and f2 on a list of inputs xs."
    return all(f1(x) == f2(x) for x in xs)


# %%
def adder(a):
    "The function adder here defines another function which adds `a` to any given number."
    "By doing this you can partially apply addition on numbers"

    def adder_a(b):
        return a + b

    return adder_a


# %%
def ensure_positive(func):
    "decorator to ensure that all arguments are non-negative"

    def wrapper(*xs):
        if any(x < 0 for x in xs):
            raise ValueError("both arguments must be non-negative")
        return func(*xs)

    return wrapper


# %%
@ensure_positive
def gcd(a, b):
    "this function calculates the GCD of given numbers in ancient way."
    while a != b:
        if a > b:
            a -= b
        if a < b:
            b -= a

    return a


# %%
@ensure_positive
def factorial(n):
    "recursive factorial function"
    if n == 0:
        return 1
    return n * factorial(n - 1)
