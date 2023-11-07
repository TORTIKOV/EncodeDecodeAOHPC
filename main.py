import random


def length_controller(key, plaintext):
    different = len(plaintext) % key
    different = key - different
    for i in range(0, different):
        plaintext += ' '
    return plaintext


def transposition_encode(key, plaintext):
    num_columns = len(plaintext) // key
    table = [[' ' for _ in range(key)] for _ in range(num_columns)]
    i = 0
    for col in range(key):
        for row in range(num_columns):
            if i < len(plaintext):
                table[row][col] = plaintext[i]
                i += 1
    encoded_message = ''.join([''.join(row) for row in table])
    return encoded_message


def transposition_decode(key, ciphertext):
    num_columns = len(ciphertext) // key
    num_rows = key
    table = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    i = 0
    for col in range(num_columns):
        for row in range(num_rows):
            table[row][col] = ciphertext[i]
            i += 1
    decoded_message = ''.join([''.join(row) for row in table])
    return decoded_message


def print_transposition_table(key, plaintext):
    num_columns = len(plaintext) // key
    num_rows = key
    table = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    for i, char in enumerate(plaintext):
        col = i % num_columns
        row = i // num_columns
        table[row][col] = char
    print("Transposition Table:")
    for row in table:
        print(' '.join(row))


print("||====================Trnasposition===================||")
# Example usage:
key = 5
message = "This is a sample message for encoding with Transposition cipher."
message_new = length_controller(key, message)
encoded_message = transposition_encode(key, message_new)
print("Encoded Message:")
print(encoded_message)
print(len(message_new))
print(len(encoded_message))
decoded_message = transposition_decode(key, encoded_message)
print("\nDecoded Message:")
print(decoded_message)
print_transposition_table(key, message_new)
print("\n\n\n||====================Cesar===================||")


def caesar_encode(text, shift):
    encoded_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encoded_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encoded_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encoded_char = char
        encoded_text += encoded_char
    return encoded_text


def caesar_decode(text, shift):
    return caesar_encode(text, -shift)


message = "This is a sample message for encoding with Caesar cipher."
shift = 3

encoded_message = caesar_encode(message, shift)
print("Encoded Message:")
print(encoded_message)

decoded_message = caesar_decode(encoded_message, shift)
print("\nDecoded Message:")
print(decoded_message)

print("\n\n\n||====================RSA===================||")


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    def witness(a, n):
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if gcd(a, n) != 1 or witness(a, n):
            return False
    return True


def generate_prime(bits):
    while True:
        potential_prime = random.getrandbits(bits)
        if is_prime(potential_prime):
            return potential_prime


def rsa_keygen(bit_length):
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi_n)
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key


def rsa_encrypt(plaintext, public_key):
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def rsa_decrypt(ciphertext, private_key):
    n, d = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)


bit_length = 128
public_key, private_key = rsa_keygen(bit_length)
message = "This is a sample message for encoding with RSA cipher."
ciphertext = rsa_encrypt(message, public_key)
print("Encoded Message:", ciphertext)
decrypted_message = rsa_decrypt(ciphertext, private_key)
print("Decrypted Message:", decrypted_message)
