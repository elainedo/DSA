def computeMnemonics(num):
    
    num_dict = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

    result = []
    if len(num) == 0:
        return result

    if len(num) == 1:
        for c in num_dict[ord(num[0])-ord('0')]:
            result.append(c)
        return result
    
    suffix = computeMnemonics(num[1:])
    for part in suffix:
        for c in num_dict[ord(num[0])-ord('0')]:
            result.append(c + part)

    return result

print(computeMnemonics('34'))