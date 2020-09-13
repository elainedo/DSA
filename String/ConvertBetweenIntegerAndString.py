def int_to_string(num):
    is_negative = False
    if num < 0: 
        num = -num
        is_negative = True
    s = []
    while num > 0:
        s.append(chr(ord('0')+num%10))
        num //= 10
    return ("-" if is_negative else "") + "".join(reversed(s))

print(int_to_string(5463))
print(int_to_string(-5463))

def string_to_int(s):
    if len(s) == 0:
        return 0
    is_negative = 1
    if s[0] == "-":
        s = s[1:]
        is_negative = -1
    
    result = 0
    for c in s:
        result = 10*result + ord(c) - ord('0')
    
    return result*is_negative

print(string_to_int("5463"))
print(string_to_int("-5463"))

    