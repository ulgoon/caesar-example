from string import ascii_uppercase as alpha


def caesar(to_encrypt: str, k: int, decode=False) -> str:
    shifted = dict(
        zip(alpha,
            alpha[(k, len(alpha)-k)[decode]:]+alpha[:(k, len(alpha)-k)[decode]]
            )
    )
    return ''.join(shifted[c] if c in alpha else c
                   for c in to_encrypt.upper())


def get_info() -> tuple:
    sentence = input('Enter Sentence to encrypt(decrypt): ')
    cipher_key = int(input('Enter key(1-25): '))
    is_encrypt = input('(E)ncrypt or (D)ecrypt? ').upper()
    is_encrypt = False if is_encrypt == 'E' else True
    return (sentence, cipher_key, is_encrypt)


if __name__ == '__main__':
    sentence, cipher_key, is_encrypt = get_info()
    print(caesar(sentence, cipher_key, is_encrypt))
#    print(caesar('Python is awesome language.', 18))
#    print(caesar(caesar('Python is awesome language.', 18), 18, True))
