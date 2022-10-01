import csv
import pandas as pd
import os
import itertools


def path_system():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, 'cedis2.xlsx')
    return my_file


def get_sheet(idx1, idx2, idx3):
    xls = pd.ExcelFile(path_system())
    sheets = xls.sheet_names
    get_date_xls = pd.read_excel(path_system(), sheet_name=sheets[3])[[idx1, idx2, idx3]].rename(
        columns={idx1: 'pasillo', idx2: 'columna', idx3: 'ubicacion'}).dropna().to_dict('records')
    return get_date_xls


def join_tables():
    list_range = []
    list_all = []
    divider = 3
    for j in range(1, 28):
        list_range.append(j)

    out_divider = [list_range[i:i + divider]
                   for i in range(0, len(list_range), divider)]
    total = len(out_divider)
    counter = 0

    for k in out_divider:
        counter += 1
        load = round((counter / total) * 100, 2)
        print("{} % --> {}".format(load, len(get_sheet(k[0], k[1], k[2]))))
        list_all.append(get_sheet(k[0], k[1], k[2]))

    flat_list = list(itertools.chain(*list_all))

    return flat_list


def export_dates():
    headers = ['pasillo', 'columna', 'ubicacion']

    name_document = input("Por favor, agrega un nombre: ")
    print(".: Cargando programa :.\n-----------------------")

    with open(name_document + '.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(join_tables())

    print("File success !!!")


if __name__ == '__main__':
    export_dates()
