import os
import shutil
#создание файла
def create_file(filename):
    try:
        with open(filename, 'w'):
            pass
        print(f"Файл '{filename}' создан.")
    except Exception as e:
        print(f"Ошибка '{filename}': {e}")
#создание папки
def create_folder(foldername):
    try:
        os.makedirs(foldername, exist_ok=True)
        print(f"Папка '{foldername}' создана.")
    except Exception as e:
        print(f"Ошибка '{foldername}': {e}")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"Файл '{filename}' удален.")
    except Exception as e:
        print(f"Ошибка '{filename}': {e}")
#Удаление папки
def delete_folder(foldername):
    try:
        shutil.rmtree(foldername)
        print(f"Папка '{foldername}' удалена.")
    except Exception as e:
        print(f"Ошибка '{foldername}': {e}")
#перемещение файла
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Файл '{source}' перемещен в '{destination}'.")
    except Exception as e:
        print(f"Ошибка '{source}' в '{destination}': {e}")
#копирование файла
def copy_file(source, destination):
    try:
        shutil.copy2(source, destination)
        print(f"Файл '{source}' скопирован в '{destination}'.")
    except Exception as e:
        print(f"Ошибка '{source}' в '{destination}': {e}")
# просмотр директории
def list_directory(path):
    try:
        print(f"Содержимое папки '{path}':")
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print(f"Ошибка при получении содержимого папки '{path}': {e}")
#изменение имени файла
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Файл '{old_name}' переименован в '{new_name}'.")
    except Exception as e:
        print(f"Ошибка переименования файла '{old_name}' в '{new_name}': {e}")

if __name__ == "__main__":
    while True:
        print("\nFile Manager Menu:")
        print("1. Создать файла")
        print("2. Создать папку")
        print("3. Удалить файла")
        print("4. Удалить папку")
        print("5. Переместить файл")
        print("6. Копировать файл")
        print("7. Вывести содержимое папки")
        print("8. Переименовать файл")
        print("9. Выход")
        choice = input("Выберите опцию: ")
        if choice == '1':
            filename = input("Название файла: ")
            create_file(filename)
        elif choice == '2':
            foldername = input("Название папки: ")
            create_folder(foldername)
        elif choice == '3':
            filename = input("Название файла: ")
            delete_file(filename)
        elif choice == '4':
            foldername = input("Название папки: ")
            delete_folder(foldername)
        elif choice == '5':
            source = input("Название файла: ")
            destination = input("Новый путь: ")
            move_file(source, destination)
        elif choice == '6':
            source = input("Название файла: ")
            destination = input("Название нового файла: ")
            copy_file(source, destination)
        elif choice == '7':
            path = input("Введите путь к папке (пустое для текущей папки): ")
            list_directory(path)
        elif choice == '8':
            old_name = input("Старое имя файла: ")
            new_name = input("Новое имя файла: ")
        elif choice == '9':
            print("Выход")
            break
        else:
            print("Ошибка")