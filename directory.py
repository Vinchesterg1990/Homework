import os
import time

directory = r'F:\Загрузки\Домашка\pythonProject1\.venv\Scripts'
directory_1 = os.path.normpath(directory)
count = 0
for root, dirs, files in os.walk(directory_1):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        count += 1
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')