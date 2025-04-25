def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result

def mod2div(dividend, divisor):
    pick = len(divisor)
    temp = dividend[0:pick]

    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp) + dividend[pick]
        pick += 1

    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)

    return temp  # remainder

def encodeData(data, divisor):
    l_key = len(divisor)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, divisor)
    codeword = data + remainder
    return codeword

# Example input
data = "1011001"
divisor = "1001"  # Generator polynomial

print(f"Original Data: {data}")
print(f"Generator: {divisor}")

codeword = encodeData(data, divisor)
print(f"Encoded Data (Data + CRC): {codeword}")

# Simulate receiver check
received = codeword  # Try modifying this to simulate error
remainder = mod2div(received, divisor)

print("Remainder after checking at receiver side:", remainder)
if '1' in remainder:
    print("Error detected in received data ❌")
else:
    print("No error detected ✅")
