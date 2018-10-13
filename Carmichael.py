import random

# Total: O(n^2)
def prime_test(N, k):                       # Storing parameters is O(n) space
    if k > N - 2:
        k = N - 2                           # O(n) space.
    if k < 0:
        k = 1
    nums = []                               # Space will eventually be O(k * n) once it is populated.
    for _ in range(k):
        n = random.randint(2, N - 1)        # O(n) space
        while n in nums:
            n = random.randint(2, N - 1)    # O(n) space
        nums.append(n)                      # O(n) space
    for num in nums:                        # Space complexity is not a product of k because the stack is cleared
                                            # after each call to mod_exp.
        if mod_exp(num, N - 1, N) != 1:     # O(n^2) space to call mod_exp
            return 'composite'
    for num in nums:                        # O(n^2) for same reason as previous for loop.
        if is_carmichael(N, nums[0]):
            return 'composite'
    return 'prime'

# Total: O(n^2)
def mod_exp(x, y, N):                       # Storing parameters is O(n) space. Function calls itself up to n times,
                                            # so space is O(n^2)
    if y == 0:
        return 1
    z = mod_exp(x, y//2, N)                 # Function call is O(n^2) space
    if y % 2 == 1:
        return (x * z**2) % N
    return z**2 % N

# Total: O(n)
def probability(k):                         # Storing parameters requires O(n) space
    return 1.0 - (1 / 2**k)

# Total: O(n^2)
def is_carmichael(N,a):                     # O(n) space to store parameters
    u = N - 1                               # O(n) space
    t = 0
    while u % 2 == 0:
        u /= 2                              # u has already been assigned, no additional space.
        t += 1                              # This loop brings t up to O(n) space by the end.
    y = N - 1                               # O(n) space
    for i in range(t + 1):                  # O(n^2) space. Executing t times does not affect space because the
                                            # stack is reset.
        x = mod_exp(a, ((2**i) * u), N)     # O(n^2) space function.
        if x == 1:
            if y != N - 1:
                return True
            else :
                return False
        else:
            y = x                           # y has already been assigned, no additional space.
