# https://leetcode.com/problems/counting-bits/

def count_bits(num):
    bit_count = 0

    while num > 0:
        bit = num % 2
        bit_count += bit
        num = num // 2

    return bit_count
