from caesar import *
from  vernam import *
import logging

# Настройка логирования
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def main():
    while True:
        # Ввод текста с клавиатуры
        plaintext = input("Введите текст для шифрования (или 'выход' для завершения): ")
        if plaintext.lower() == 'выход':
            print("Завершение программы.")
            break

        # Выбор шифра
        print("Выберите метод шифрования:")
        print("1. Шифр Цезаря")
        print("2. Шифр Вернама")
        choice = input("Введите номер метода (1 или 2): ")

        if choice == '1':
            shift = int(input("Введите сдвиг для шифра Цезаря (от 1 до 25): "))
            ciphertext = caesar_encrypt(plaintext, shift)
            print(f"Зашифрованный текст (Цезарь): {ciphertext}")

            decrypted_text = caesar_decrypt(ciphertext, shift)
            print(f"Дешифрованный текст (Цезарь): {decrypted_text}")

            # Логирование результата
            logging.info(f"Шифрование (Цезарь): Входной текст: {plaintext}, Результат: {ciphertext}")
            logging.info(f"Дешифрование (Цезарь): Входной текст: {ciphertext}, Результат: {decrypted_text}")

        elif choice == '2':
            key = generate_random_key(len(plaintext))
            encrypted_vernam = vernam_encrypt(plaintext, key)
            print(f"Зашифрованный текст (Вернам): {encrypted_vernam}")

            decrypted_vernam = vernam_decrypt(encrypted_vernam, key)
            print(f"Дешифрованный текст (Вернам): {decrypted_vernam}")

            # Логирование результата
            logging.info(f"Шифрование (Вернам): Входной текст: {plaintext}, Результат: {encrypted_vernam}")
            logging.info(f"Дешифрование (Вернам): Входной текст: {encrypted_vernam}, Результат: {decrypted_vernam}")

        else:
            print("Неверный выбор метода.")

if __name__ == "__main__":
    main()