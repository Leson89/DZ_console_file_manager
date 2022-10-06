import os
import sys
import shutil

#Создание файлов и папок
def new():
    while True:
        print('1. создать файл')
        print('2. создать папку')
        print('3. выход')
        choice = input('Выберите пункт меню')
        if choice == '1':
            new_file = input('Введите название файла:')
            try:
                file = open(new_file, 'r')
            except:
                file = open(new_file, 'w')
        elif choice == '2':
            folder = input('Введите название папки:')
            if not os.path.isdir(folder):
                os.mkdir(folder)
        elif choice == '3':
            break
        else:
            print('Неверный пункт меню')
#Удаление файлов и папок
def dellet():
    while True:
        print('1. удалить файл')
        print('2. удалить папку')
        print('3. выход')
        choice = input('Выберите пункт меню')
        if choice == '1':
            os.remove(input('Введите название файла для удаления:'))
        elif choice == '2':
            Folder_remove = input('Введите название папки')
            if os.path.isfile:
                shutil.rmtree(Folder_remove)

            else:
                os.rmdir(Folder_remove)

        elif choice == '3':
            break
        else:
            print('Неверный пункт меню')
#Копировать файл/папку
def copy():
    while True:
        print('1. Копировать файл')
        print('2. Копировать папку')
        print('3. выход')
        choice = input('Выберите пункт меню')
        if choice == '1':
            shutil.copy(input('Название фала'), input('Новое название фала'))
        elif choice == '2':
            shutil.copytree(input('Название папки'), input('Новое название папки'))
        elif choice == '3':
            break
        else:
            print('Неверный пункт меню')

