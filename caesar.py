from string import ascii_uppercase as alpha


def caesar(to_encrypt: str, k: int, decode=False) -> str:
    shifted = dict(
        zip(alpha,
            alpha[(k, len(alpha)-k)[decode]:]+alpha[:(k, len(alpha)-k)[decode]]
            )
    )
    return ''.join(shifted[c] if c in alpha else c
                   for c in to_encrypt.upper())


if __name__ == '__main__':
    print(caesar('Python is awesome language.', 18))
    print(caesar(caesar('Python is awesome language.', 18), 18, True))
