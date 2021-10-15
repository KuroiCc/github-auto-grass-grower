import sys
from datetime import datetime, timedelta

if __name__ == "__main__":
    path = sys.argv[1]
    # path = "./test/records.txt"
    fmt = "%Y-%m-%d %X"
    str_list = []
    with open(path) as file:
        lines = file.readlines()

    num_of_day = (
        datetime.strptime(lines[-1][:19], fmt) - datetime.strptime(lines[0][:19], fmt)
    ).days + 1
    day = datetime.strptime(lines[0][:19], fmt)
    index = 0
    for i in range(num_of_day):
        a = lines[index][:10]
        b = day.strftime("%Y-%m-%d")
        if lines[index][:10] == day.strftime("%Y-%m-%d"):
            str_list.append("■")
            index += 1
        else:
            str_list.append("□")

        day += timedelta(days=1)

    for i in range(7):
        for j in range(len(str_list) // 7):
            index = i + 7 * j
            print(str_list[index], end=" ")
        if i < len(str_list) % 7:
            print(str_list[i + 7 * (j + 1)], end=" ")
        print()
