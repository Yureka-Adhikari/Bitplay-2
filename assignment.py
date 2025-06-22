def reverse_bits(n):
    bit_length = n.bit_length()
    result = 0

    for i in range(bit_length):
        bit = (n >> i) & 1
        result |= (bit << (bit_length - 1 - i))

    return result

num = int(input("Enter a non-negative integer: "))
reversed_num = reverse_bits(num)
print("Reversed bit number:", reversed_num)

