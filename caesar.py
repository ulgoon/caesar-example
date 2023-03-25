from string import ascii_uppercase as alpha


def caesar(to_encrypt: str, k: int, decode=False) -> str:
    shifted = dict(
        zip(alpha,
            alpha[(k, len(alpha)-k)[decode]:]+alpha[:(k, len(alpha)-k)[decode]]
            )
    )
    return shifted


if __name__ == '__main__':
    print(caesar('a', 18))
