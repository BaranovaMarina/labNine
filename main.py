def process_files():
    try:
        # а) Створення текстового файлу TF26_1 із рядками різної довжини
        with open("TF26_1.txt", "w") as file1:
            file1.writelines([
                "Hello World\n",
                "Python Programming\n",
                "AI and Machine Learning\n",
                "Text File Example\n"
            ])
        print("Файл TF26_1.txt створено.")

        # б) Читання файлу TF26_1, заміна великих літер на малі, запис у TF26_2
        with open("TF26_1.txt", "r") as file1:
            lines = file1.readlines()
            modified_lines = [line.lower() for line in lines]  # Перетворення в малі літери

        with open("TF26_2.txt", "w") as file2:
            file2.writelines(modified_lines)
        print("Файл TF26_2.txt створено з модифікованим вмістом.")

        # в) Читання файлу TF26_2 і друк його вмісту
        with open("TF26_2.txt", "r") as file2:
            print("Вміст файлу TF26_2.txt:")
            for line in file2:
                print(line.strip())  # strip() для видалення зайвих переносів рядків

    except FileNotFoundError as e:
        print(f"Помилка: файл не знайдено. {e}")
    except IOError as e:
        print(f"Помилка вводу/виводу: {e}")
    except Exception as e:
        print(f"Невідома помилка: {e}")


# Виклик функції
process_files()
