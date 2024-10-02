import time
from datetime import datetime
from threading import Thread

time_start = datetime.now()

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(f'Какое-то слово № {i}\n' for i in range(1,word_count+1))
        time.sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')

func_1 = write_words(10, 'example1.txt')
func_2 = write_words(30, 'example2.txt')
func_3 = write_words(200, 'example3.txt')
func_4 = write_words(100, 'example4.txt')

time_end = datetime.now()
time_fin = time_end - time_start
print(f'Работа функции: {time_fin}')

time_start = datetime.now()

thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
time_fin = time_end - time_start
print(f'Работа потоков: {time_fin}')