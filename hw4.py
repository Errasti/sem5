with open('txt1', 'r') as data:
    crypt = data.read()


def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(crypt)
print(str_code)

with open('txt2', 'w') as data:
    data.write(str_code)


def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


with open('txt3', 'w') as data:
    data.write(decoding_rle(str_code))


