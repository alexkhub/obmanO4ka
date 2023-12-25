import random
from pathlib import Path
import os
from colorama import init, Fore

init()
random_marks = [' ', '  ', '\n', '   ', ' ', ' ', '', '  ', ' ', ' ', '']
task_list = ['1-1.py', '2-1.py' ]  # укажите все файлы
url = Path('1_tasks')
url2 = Path('2_updated_tasks')
flag = True

for task_name in task_list:
    file_to_open = url / task_name
    file_to_write = url2 / task_name
    try:
        os.remove(file_to_write)
        print(Fore.GREEN + f'{task_name} успешно перезаписан ')
    except FileNotFoundError:
        pass

    try:
        f = open(file_to_open)
    except FileNotFoundError:
        print(Fore.RED + f"{task_name} - файл не обнаружен")
        raise SystemExit

    for row in f:
        random_mark = random.choice(random_marks)
        try:
            with open(file_to_write, 'a') as f2:
                if '\n' in row:
                    line = f'{row[:-1]}{random_mark}\n'
                else:
                    line = f'{row}{random_mark}'
                f2.seek(0, 2)
                f2.write(line)
        except FileNotFoundError:
            open(file_to_write, 'w').write(row)
    f.close()
    f2.close()
print(Fore.GREEN + "Файлы созданы")
