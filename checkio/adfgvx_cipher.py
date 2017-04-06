"""
    https://py.checkio.org/mission/adfgvx-cipher/
"""
from itertools import cycle
from collections import defaultdict


secret_key = 'ADFGVX'


def encode(message, secret_alphabet, keyword):
    encrypted = ''
    for char in message:
        found_at = secret_alphabet.find(char.lower())
        if found_at != -1:
            code = secret_key[found_at // 6] + secret_key[found_at % 6]
            encrypted += code

    table = defaultdict(list)
    for k, v in zip(cycle(sorted(list(set(keyword)), key=keyword.index)), encrypted):
        table[k].append(v)

    result = []
    for k in sorted(table):
        result.append(''.join(table[k]))
    return ''.join(result)


def decode(message, secret_alphabet, keyword):
    # build decrypt table
    keyword = sorted(list(set(keyword)), key=keyword.index)
    remainder = len(message) % len(keyword)
    decrypt_table = {key: len(message) // len(keyword) + (1 if i < remainder else 0)
                     for i, key in enumerate(keyword)}

    temp_message = message[:]
    for key in sorted(keyword):
        bite_length = decrypt_table[key]
        decrypt_table[key] = temp_message[:bite_length]
        temp_message = temp_message[bite_length:]

    encrypted = ''
    for key in cycle(keyword):
        encrypted += decrypt_table[key][:1]
        decrypt_table[key] = decrypt_table[key][1:]
        if len(encrypted) == len(message):
            break

    result = ''
    for row, column in zip(encrypted[::2], encrypted[1::2]):
        result += secret_alphabet[secret_key.index(row) * 6 + secret_key.index(column)]
    return result


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"
