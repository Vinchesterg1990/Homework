import time
from threading import Thread

def wite_words(word_count, file_name):
    with open ('example1.txt', 'w', encoding= 'utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

if __name__ == '__main__':
    start_time_1 = time.time()
    wite_words(10, 'example1.txt')
    wite_words(30, 'example2.txt')
    wite_words(200, 'example3.txt')
    wite_words(100, 'example4.txt')
    end_time_1 = time.time()
    res_time_1 = end_time_1 - start_time_1
    print(res_time_1)
    start_time_2 = time.time()
    a1 = Thread(target=wite_words, args=(10, 'example5.txt'))
    a2 = Thread(target=wite_words, args=(30, 'example6.txt'))
    a3 = Thread(target=wite_words, args=(200, 'example7.txt'))
    a4 = Thread(target=wite_words, args=(100, 'example8.txt'))

    a1.start()
    a2.start()
    a3.start()
    a4.start()

    a1.join()
    a2.join()
    a3.join()
    a4.join()

    end_time_2 = time.time()
    res_time_2 = end_time_2-start_time_2
    print(res_time_2)



