import os
import random

def vernam_encrypt(plaintext, key):
    """Шифрование текста с помощью шифра Вернама."""
    if len(plaintext) != len(key):
        raise ValueError("Длина текста и ключа должны совпадать.")

    encrypted_text = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return encrypted_text


def vernam_decrypt(ciphertext, key):
    """Дешифрование текста с помощью шифра Вернама."""
    return vernam_encrypt(ciphertext, key)

def generate_random_key(length):
    """Генерация случайного ключа заданной длины."""
    return ''.join(chr(random.randint(0, 255)) for _ in range(length))
