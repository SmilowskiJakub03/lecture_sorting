import os
import csv
from numpy import random
def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    dtst = {}
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r",) as file:

        tmp_i = csv.DictReader(file)

        dtst = {}

        for row in tmp_i:
            for hdr, val in row.items():
                if hdr not in dtst:
                    dtst[hdr] = [int(val)]
                else:
                    dtst[hdr].append(int(val))


    return dtst
tst = read_data("numbers.csv")
print(tst)



def selection_sort(number_list, direction):
    """

    """
    ln = len(number_list)


    for i in range(ln):
        min_index = i

        for j in range(i + 1, ln):
            if direction == 0:
                if number_list[j] < number_list[min_index]:
                    min_index = j

            elif direction == 1:
                if number_list[j] > number_list[min_index]:
                    min_index = j

        (number_list[i], number_list[min_index]) = (number_list[min_index], number_list[i])
    return number_list


def bubble_sort(number_list):
    """

    """
    ln = len(number_list)
    for i in range(ln - 1):
        for j in range(0, ln - i - 1):
            swpd = False
            if number_list[j] > number_list[j + 1]:
                swpd = True
                (number_list[j], number_list[j + 1]) = (number_list[j + 1], number_list[j])
        if not swpd:
            return number_list

def insertion_sort(number_list):
    ln = len(number_list)
    for i in range(1, ln):
        tp = number_list[i]
        j = i - 1
        while j >= 0 and tp < number_list[j]:
            number_list[j + 1] = number_list[j]
            j -= 1
            number_list[j + 1] = tp

    return number_list



def main():
    my_lst = random.randint(200, size=(10))
    print(my_lst)

    tst_sel = selection_sort(my_lst, 0)
    print(tst_sel)

    tst_bub = bubble_sort(my_lst)
    print(tst_bub)

    tst_ins = insertion_sort(my_lst)
    print(tst_ins)


if __name__ == '__main__':
    main()
