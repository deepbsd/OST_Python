#!/usr/local/bin/python3


def get_text():
    """Get user text to encode"""
    user_text = input("Please enter text: ")
    return user_text

def encode_text(user_text):
    """ encode user text"""
    # reverse the user string. Add 1 to the ascii value
    # of the character and print that ascii character.
    r_ciph = ""
    for c in reversed(user_text):
        r_ciph = r_ciph + chr(ord(c)+1)
    return r_ciph

def decode_text(r_ciph):
    """ decodes and returns text (stored in r_ciph) """
    # Do the reverse operation for debugging and checking!
    orig_text = ""
    for c in reversed(r_ciph):
        orig_text = orig_text + chr(ord(c)-1)
    return orig_text


if __name__ == "__main__":


    while True:
        in_text = encode_text(get_text())
        if in_text == "":
            print("\nbye now!\n")
            break
        print("\nCoded text is: {0}".format(in_text))
        out_text = decode_text(in_text)
        print("\nDecoded text is: {0}\n".format(out_text))




