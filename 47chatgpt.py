# Initial message and its title-cased version
a = "this is simple and easy version of naze Enigma machine made by pristane"
print(a.title())

# Encoding part
print("To use this, enter your code:")
b = input()

# Substitution dictionary for encoding
if len(b) >= 3:
    pref = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i',
        'i': 'o', 'j': 'P', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h',
        'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b',
        'y': 'n', 'z': 'm', '5': '6', '4': '7', '3': '8', '2': '9', '1': '0'
    }

    encoded_message = ''.join(pref.get(l, l) for l in b)
    print("This is your encoded message:\n" + encoded_message)

    # Decorative output
    print("""             
          ░░░░░░░░░░░░░░░▄▀▄░░░░░░░░░░░░░░░
          ░░░░░░░░░░░░░▄▀░░░▀▄░░░░░░░░░░░░░
          ░░░░░░░░░░░▄▀░░░░▄▀█░░░░░░░░░░░░░
          ░░░░░░░░░▄▀░░░░▄▀░▄▀░▄▀▄░░░░░░░░░
          ░░░░░░░▄▀░░░░▄▀░▄▀░▄▀░░░▀▄░░░░░░░
          ░░░░░░░█▀▄░░░░▀█░▄▀░░░░░░░▀▄░░░░░
          ░░░▄▀▄░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░░░
          ░▄▀░░░▀▄░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░
          ░█▀▄░░░░▀▄░█▀░░░░░░░▀█░▀▄░▀▄░▄▀█░
          ░▀▄░▀▄░░░░▀░░░░▄█▄░░░░▀▄░▀▄░█░▄▀░
          ░░░▀▄░▀▄░░░░░▄▀░█░▀▄░░░░▀▄░▀█▀░░░
          ░░░░░▀▄░▀▄░▄▀░▄▀░█▀░░░░▄▀█░░░░░░░
          ░░░░░░░▀▄░█░▄▀░▄▀░░░░▄▀░▄▀░░░░░░░
          ░░░░░░░░░▀█▀░▄▀░░░░▄▀░▄▀░░░░░░░░░
          ░░░░░░░░░░░░░█▀▄░▄▀░▄▀░░░░░░░░░░░
          ░░░░░░░░░░░░░▀▄░█░▄▀░░░░░░░░░░░░░
          ░░░░░░░░░░░░░░░▀█▀░░░░░░░░░░░░░░░""")

else:
    print("Please enter more than three letters.")

# Decoding part
print("Now let's decode it:")
j = input("Enter your code to decode:\n")

# Substitution dictionary for decoding
if len(j) >= 3:
    pref2 = {
        'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g', 'i': 'h',
        'o': 'i', 'P': 'j', 'a': 'k', 's': 'l', 'd': 'm', 'f': 'n', 'g': 'o', 'h': 'p',
        'j': 'q', 'k': 'r', 'l': 's', 'z': 't', 'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x',
        'n': 'z', 'm': 'y', '0': '1', '9': '2', '8': '3', '7': '4', '6': '5'
    }

    decoded_message = ''.join(pref2.get(l, l) for l in j)
    print("This is your decoded message:\n" + decoded_message)

    # Decorative output
    print("""
          ████╗░░░████████████╗
          ████║░░░████████████║
          ████║░░░████╔═══════╝
          ████║░░░████║░░░░░░░░
          ████████████████████╗
          ████████████████████║
          ╚═══════████╔═══████║
          ░░░░░░░░████║░░░████║
          ████████████║░░░████║
          ████████████║░░░████║
          ╚═══════════╝░░░╚═══╝""")
else:
    print("Input too short. Please enter more than three letters.")
