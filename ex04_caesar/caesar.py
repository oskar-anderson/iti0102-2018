"""Encode and decode Caesar cipher."""


def encode(message: str, shift: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    if alphabet:
        pass
    ciphered_message = ""
    for c in message:
        if ord(c) in range(65, 91):
            alphabet = ord(c) + shift
            while alphabet > ord("Z"):
                alphabet -= 26
            while alphabet < ord("A"):
                alphabet += 26
            final_letter = chr(alphabet)
            ciphered_message += final_letter
        elif ord(c) in range(97, 123):
            alphabet = ord(c) + shift
            while alphabet > ord("z"):
                alphabet -= 26
            while alphabet < ord("a"):
                alphabet += 26
            final_letter = chr(alphabet)
            ciphered_message += final_letter
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
        if ord(c) in range(65, 91):
            alphabet = ord(c) - shift
            while alphabet > ord("Z"):
                alphabet -= 26
            while alphabet < ord("A"):
                alphabet += 26
            final_letter = chr(alphabet)
            un_ciphered_message += final_letter
        elif ord(c) in range(97, 123):
            alphabet = ord(c) - shift
            while alphabet > ord("z"):
                alphabet -= 26
            while alphabet < ord("a"):
                alphabet += 26
            final_letter = chr(alphabet)
            un_ciphered_message += final_letter
    return un_ciphered_message


if __name__ == "__main__":
    print(encode("hello HELLO", 27))  # ifmmp
    print(decode("ifmmp", 28))  # hello
    print(encode("Large Shift", 83))
    print(encode("Negative", -3))
    print(encode("symbols !.,:;", 1))
    # WRITE THE REMAINING EXAMPLES YOURSELF!

    # larger shift

    # negative shift

    # shift > alphabet.length

    # case sensitivity

    # misc symbols (.,:; etc.)

    # ...
