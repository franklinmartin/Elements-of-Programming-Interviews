import sys

def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

#O(1) computations per bit
#O(n) time complexity
#n bits to repretent integer
#4 bit : 12 (1100)

input = int(sys.argv[1])
print(count_bits(input))


