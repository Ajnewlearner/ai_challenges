def bitmanipulate(s):
    result = ''
    for char in s:
        ascii = ord(char)
        binary = format(ascii,'08b')
        result +=binary
    return result

# bi = bitmanipulate('dffd')
# print(bi)
print(bitmanipulate('d'))
chr(bitmanipulate('d'))

# print(int("10")+ float("5"))