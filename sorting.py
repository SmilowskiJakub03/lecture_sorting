import os
import csv

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
def main():
    pass


if __name__ == '__main__':
    main()
