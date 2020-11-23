from math import pow


def hash_key(string):
    key = ord(string[0])
    prime = 101
    for i in range(1, len(string)):
        key += ord(string[i]) * pow(prime, i)
    return key


def rabin_karp(patt, text):
    n, m = len(text), len(patt)
    out = []
    prime = 101
    patt_key = hash_key(patt)
    init = hash_key(text[0:m])
    if patt_key == init and text[0:m] == patt:
        out.append(0)
    for i in range(1, n - m + 1):
        init -= ord(text[i-1])
        init //= prime
        init += ord(text[i+m-1]) * pow(prime, m-1)
        if patt_key == init and text[i:i+m] == patt:
            out.append(i)
    return out


def main():
    patt = input().rstrip()
    text = input().rstrip()
    print(*rabin_karp(patt, text))


if __name__ == '__main__':
    main()