# CS50P Week8
# Objective: A class representing a cookie jar with
# deposit/withdraw functionality
# Features:
#   - Customizable capacity (default: 12 cookies)
#   - Cookie deposit and withdrawal with validation
#   - Visual representation using cookie emoji
# Usage:
#   jar = Jar()          # Default jar (12 cookies max)
#   jar.deposit(5)       # Add 5 cookies
#   jar.withdraw(2)      # Remove 2 cookies
#   print(jar)           # Displays "🍪🍪🍪" (if size=3)
# Validation Rules:
#   - Capacity must be a positive integer
#   - Cannot deposit beyond capacity
#   - Cannot withdraw more than available cookies
#   - All operations require non-negative integers
class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError
        if self._size - n < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
