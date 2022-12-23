import os
import sys
import shutil

from victory.famouse_people import birthday as game
from bank import finance as bill
from file_manager import actions



while True:
    print('1. создать файл/папку')
    print('2. удалить файл/папку')
    print('3. копировать файл/папку')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. Выход')


    choice = input('Выберите пункт меню')
    if choice == '1':
        actions.new()
    elif choice == '2':
        actions.dellet()
    elif choice == '3':
        actions.copy()
    elif choice == '4':
        print(sys.path)
    elif choice == '5':
        folders = list(filter(os.path.isdir, os.listdir(os.curdir)))
        print('Файлы в текущей директории')
        print(folders)
    elif choice == '6':
        files = list(filter(os.path.isfile, os.listdir(os.curdir)))
        print('Файлы в текущей директории')
        print(files)
    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print('Грабко Олесь Геннадьевич')
    elif choice == '9':
         game()
    elif choice == '10':
        bill.bill_program()
    elif choice == '11':
        os.chdir(input('Введите название директории:'))
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')