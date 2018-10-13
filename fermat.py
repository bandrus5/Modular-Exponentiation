import random

def prime_test(N, k):                       # Assume parameters are n bits long.  Storing parameters is O(n) space
    if k > N - 2:                           # This is a safety check for inputs. Subtraction and comparison are O(n) time.
        k = N - 2                           # O(n) time and space.
    if k < 0:                               # Another O(n) time safety check on inputs. Constant space if the body is executed.
        k = 1
    nums = []                               # Constant time. Space will eventually be O(k * n) once it is populated.
    for _ in range(k):                      # Loop executes k times,
        n = random.randint(2, N - 1)        # Constant time, O(n) space
        while n in nums:                    # Executes an unknown number of times, but average case shouldn't be more than O(n^2) times
            n = random.randint(2, N - 1)    # O(n) time, O(n) space
        nums.append(n)                      # O(n) time and space
    for num in nums:                        # Runs k times and executes a O(n^2 log(n)) function. Total time is O(k n^2 log(n)). O(n log(n)) space from function call.
        if mod_exp(num, N - 1, N) != 1:     # O(n^2 log(n)) time
            return 'composite'
    for num in nums:                        # For loop runs k times and calls a O(n^3 log(n)) function. Executes in O(k n^3 log(n)) time. O(n log(n)) space from function
        if is_carmichael(N, nums[0]):
            return 'composite'              # Returning 'carmichael' here would report likely carmichael numbers.
    return 'prime'                          # Only executes if the number passed all fermat and carmichael tests. Constant time / space.


def mod_exp(x, y, N):                       # Assume all numbers are at most n bits long. Function runs once in O(n^2) time. It may be called recursively up to log(n)
                                            # times, so one function call could be as much as O(n^2 log(n)) time. O(n) space to stare parameters, and with recursion
                                            # it may store up to a log(n) number of n bit z values. Total space is O(n log(n))
    if y == 0:                              # Constant time, no space.
        return 1
    z = mod_exp(x, y//2, N)                 # The division is O(n^2) time, the function called recursively is O(n^2) time. The entire line is O(n^2).
    if y % 2 == 1:                          # Modulo takes O(n) time
        return (x * z**2) % N               # This is multiple O(n^2) operations added together, which is still O(n^2) time.
    return z**2 % N                         # O(n^3) time


def probability(k):                         # Simple formula. Each test we run is at least 50% likely to reveal a composite number, so the probability that
                                            # a number we found to be prime is not actually prime is (1/2) ^ k. This means the probability it IS prime is
                                            # 1 - 1 / (2^k).
    return 1.0 - (1 / 2**k)                 # It is extremely unlikely that 2^k will exceed 64 bits, so this function should run in constant time with O(n) stize.
                                            # If it did exceed 64 bits, it would take O(n^2) time and O(n) size.


def is_carmichael(N,a):                     # Assume all parameters have at most n bits. Total run time is O(n^3 log(n)) and maximum space is O(n log(n)) from The
                                            # mod_exp function call.
    u = N - 1                               # O(n) time, O(n) space
    t = 0                                   # O(1) time and space.
    while u % 2 == 0:                       # Each loop cuts u in half, so it will execute O(log(n)) times. Longest step is O(n^2), so total time is O(n^2 log(n))
        u /= 2                              # O(n^2) time
        t += 1                              # constant time (as long as t never exceeds 64 bits...which is a safe assumption)
    y = N - 1                               # We set this to N - 1 so if the first x value comes out to 1, the function will return false. O(n) time.
    for i in range(t + 1):                  # Executes t + 1 times, longest step takes O(n^2 log(n)) time, so we have O(t n^2 log(n)) run time where t is <= n
        x = mod_exp(a, ((2**i) * u), N)     # Function takes O(n^2 log(n)) time to execute and uses O(n log(n)) space.
        if x == 1:                          # Constant time
            if y != N - 1:                  # O(n) time
                return True                 # O(1) time
            else :                          # O(1) time
                return False                # O(1) time
        else:                               # O(1) time
            y = x                           # O(n) in the rare case where x exceeds 64 bits, O(n) space.
