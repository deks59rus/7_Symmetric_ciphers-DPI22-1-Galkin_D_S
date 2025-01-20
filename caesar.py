def caesar_encrypt(plaintext, shift):
    """Шифрование текста с помощью шифра Цезаря."""
    encrypted_text = ""
    for char in plaintext:
        if 'A' <= char <= 'Z':  # Проверяем, является ли символ заглавной латинской буквой
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        elif 'a' <= char <= 'z':  # Проверяем, является ли символ строчной латинской буквой
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
        elif 'А' <= char <= 'Я':  # Проверяем, является ли символ заглавной русской буквой
            encrypted_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            encrypted_text += encrypted_char
        elif 'а' <= char <= 'я':  # Проверяем, является ли символ строчной русской буквой
            encrypted_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Не шифруем символы, не являющиеся буквами
    return encrypted_text
def caesar_decrypt(ciphertext, shift):
    """Дешифрование текста с помощью шифра Цезаря."""
    return caesar_encrypt(ciphertext, -shift)

def crack_caesar(ciphertext):
    """Восстанавливает текст, зашифрованный шифром Цезаря, без знания ключа."""
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")