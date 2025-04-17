import os
import csv
from numpy import random
def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """

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


def selection_sort(numlist,direc= 0):
    """

    :param numlist:
    :param direction:
    :return:
    """

    for i in range(len(numlist)):
        minim = i
        for j in range(i+1, len(numlist)):
            if direc == 0:
                if numlist[j] < numlist[minim]:
                    minim = j
            else:
                if numlist[j] > numlist[minim]:
                    minim = j


        numlist[i], numlist[minim] = numlist[minim], numlist[i]

    return numlist



def main():
    data = read_data("numbers.csv")

    for i in data.keys():
        print(selection_sort(data[i],1))

if __name__ == '__main__':
    main()
