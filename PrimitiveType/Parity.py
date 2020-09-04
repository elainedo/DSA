# The parity of a binary word is 1 if the number of 1s is odd
# Otherwise, it is 0

def parity(x):
    result = 0
    while x:
        result ^= x&1
        x >>= 1
    return result

print(parity(11))