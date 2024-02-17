sentence = input("Введите текстовое предложение: ")
file_path = input("Ведите путь к файлу (или нажмите Enter для перевода в 'text'): ") or "text"

with open(file_path, "w") as file:
    file.write(sentence[::-1])

with open(file_path, "r") as file:
    print("Содержимое файла:")
    print(file.read())
