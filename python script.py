# -*- coding: utf-8 -*-
#Kaspersky Task

# Подключение необходимых библиотек и модуелей
import hashlib
import random
import argparse
import string

# Переменные для выполнения программы (НЕ ИЗМЕНЯЕМЫЕ)
rand_str_for_hash = ""
hash_object = ""
first_elm_hash = ""
second_elm_hash = ""

# Переменные для выполнения программы (ИЗМЕНЯЕМЫЕ ПО ЖЕЛАНИЮ)
parser = argparse.ArgumentParser(description='Help по выполнению программы создания md5 hash по заданию')
parser.add_argument("-n", "--numb", default=10, help="Число символов генерируемой последовательности для создания md5 hash")
parser.add_argument("-m", "--match", default="00", help="Начальное значение с которого должен начинаться hash")
parser.add_argument("-f", "--file", default="something.txt", help="Файл для сохранения полученных результатов")
args = parser.parse_args()
gen_N = int(args.numb)
search_first_hash_elem = args.match[0]
search_second_hash_elem = args.match[1]
file_name = args.file

# Цикл для создания md5 hash с начальными элементами от входной последовательности длинной gen_N
while True:
  if search_first_hash_elem in first_elm_hash and search_second_hash_elem in second_elm_hash:
    break
  else:
    rand_str_for_hash = "".join(random.choice(string.ascii_uppercase + string.digits) for i in range(gen_N))
    hash_object = hashlib.md5(rand_str_for_hash.encode())
    first_elm_hash = hash_object.hexdigest()[0]
    second_elm_hash = hash_object.hexdigest()[1]

# Результат полученный в ходе выполнения цикла
temp_str_result = "Random str: " + rand_str_for_hash + " " + "Hash: " + hash_object.hexdigest()

# Создание файла для хранения результата hash функции
file_name_str = str(file_name)
f = open(file_name_str, 'a')
j = 0
while j < 50000:
  f.write(" " + "\n")
  j = j + 1
else:
  f.close()

# Запись полученного значения hash функции в созданный файл в случайную свободную строку (от 0 до 50000)
temp_write_elem = str(temp_str_result)
random_line_to_write = random.randint(0, 50000)

f = open(file_name_str, 'r')
all_in_file = f.readlines()

i = 0

while i < 100:
  if " " in all_in_file[random_line_to_write]:
    end_write = []
    end_write = end_write + all_in_file[:random_line_to_write] + [temp_write_elem] + all_in_file[random_line_to_write:]
    f.close()
    f = open(file_name_str, 'w')
    for line in end_write:
        f.write(line)
    f.close()
    break
  else:
    random_line_to_write = random.randint(0, 50000)
    i = i + 1
else:
  print("Недостаточно свободных строк")