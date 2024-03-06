import os
import time

directory = "путь_к_каталогу"

for root, dirs, files in os.walk(directory):
    for file_name in files:
        full_path = os.path.join(root, file_name)
        mtime = os.path.getmtime(full_path)
        size = os.path.getsize(full_path)
        parent_dir = os.path.dirname(full_path)

        print(f"Файл: {full_path}")
        print(f"Время последнего изменения: {time.ctime(mtime)}")
        print(f"Размер файла: {size} байт")
        print(f"Родительская директория: {parent_dir}")
        print("-" * 50)
