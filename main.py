from caesar import *
from  vernam import *
import logging

# Настройка логирования
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def print_log(n):
    """Вывод последних n строк из файла лога."""
    try:
        with open('log.txt', 'r', encoding='cp1251') as log_file:
            lines = log_file.readlines()
            # Выводим последние n строк
            for line in lines[-n:]:
                print(line.strip())
    except FileNotFoundError:
        print("Файл лога не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

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
        print("3. Печать лога")
        choice = input("Введите номер метода (1, 2 или 3): ")

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

        elif choice == '3':
            try:
                n = int(input("Введите количество последних строк для вывода из лога: "))
                print_log(n)
            except ValueError:
                print("Пожалуйста, введите корректное целое число.")

        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()