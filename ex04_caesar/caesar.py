"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    ciphered_message = ""
    for c in message:
        if c in alphabet.upper():
            alphabet = alphabet.upper()
            shifted_index = alphabet.index(c) + shift
            ciphered_message += alphabet[shifted_index % len(alphabet)]
        elif c in alphabet.lower():
            alphabet = alphabet.lower()
            shifted_index = alphabet.index(c) + shift
            ciphered_message += alphabet[shifted_index % len(alphabet)]
        else:
            ciphered_message += c
    return ciphered_message


def decode(message: str, shift: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    if alphabet:
        pass
    un_ciphered_message = ""
    for c in message:
        if c in alphabet.upper():
            alphabet = alphabet.upper()
            shifted_index = alphabet.index(c) - shift
            un_ciphered_message += alphabet[shifted_index % len(alphabet)]
        elif c in alphabet.lower():
            alphabet = alphabet.lower()
            shifted_index = alphabet.index(c) - shift
            un_ciphered_message += alphabet[shifted_index % len(alphabet)]
        else:
            un_ciphered_message += c
    return un_ciphered_message


if __name__ == "__main__":
    print(encode("hello HELLO", 1))  # ifmmp
    print(decode("ifmmp", 1))  # hello
    print(encode("Labc", 52))
    print(encode("Negative", -3))
    print(encode("symbols !.,:;", 1))
    # WRITE THE REMAINING EXAMPLES YOURSELF!

    # larger shift

    # negative shift

    # shift > alphabet.length

    # case sensitivity

    # misc symbols (.,:; etc.)

    # ...
