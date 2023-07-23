from Crypto.Util.number import long_to_bytes


state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return [matrix[index][raw] for raw in range(len(matrix)) for index in range(len(matrix))]

def add_round_key(s, k):
    for raw in range(len(s)):

        for index in range(len(s)):
            s[index][raw] = s[index][raw] ^ k[index][raw]
    
add_round_key(state, round_key)
print(matrix2bytes(state))
str = ''.join([chr(xor_result) for xor_result in matrix2bytes(state)])
print(str)
# list_xor_key = add_round_key(state, round_key)
# for i in range(len(s)**2):
# result = int(''.join(bin(xor_key)[2:].zfill(8) for xor_key in list_xor_key),base=2)
# print(long_to_bytes(result).decode())
