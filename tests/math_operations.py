import sys

def add(a, b):
    return a + b

print("=== Running Unit Tests")

# Intentionally making it FAIL first (2+2 != 5)
expected = 4
result = add(2, 2)

if result == expected:
    print("TEST PASSED: MAth works!")
    sys.exit(0)

else:
    print(f"TEST FAILED: Expected {expected} but got {result}")
    sys.exit(1)