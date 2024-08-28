import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    file = open(name, 'r')
    while True:
        line = file.readline()
        all_data.append(line)
        if not line:
            break
    file.close

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

for file in files:
    data = read_info(file)
# time_start = datetime.now()
# for i in files:
#    read_info(i)
# time_end = datetime.now()
# time_res = time_end - time_start
# print(time_res)
if __name__ == '__main__':
    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res)
