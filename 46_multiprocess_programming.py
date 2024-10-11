import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, "r") as file:
        while line := file.readline():
            all_data.append(line)


if __name__ == "__main__":
    # Линейный вызов
    start = datetime.datetime.now()
    files = [f"./file {i}.txt" for i in range(1, 5)]
    for file in files:
        read_info(file)
    finish = datetime.datetime.now()
    print(finish - start, "(линейный)", sep=" ")

    # Многопроцессный вызов
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        files = [f"./file {i}.txt" for i in range(1, 5)]
        pool.map(read_info, files)
        finish = datetime.datetime.now()
        print(finish - start, "(многопроцессный)", sep=" ")
