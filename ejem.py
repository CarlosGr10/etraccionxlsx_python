import csv
import pandas as pd
import os
import itertools
from time import sleep
from tqdm import tqdm


def path_system():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, 'e5a.xlsx')
    return my_file


def get_sheet():
    xls = pd.ExcelFile(path_system())
    sheets = xls.sheet_names
    get_date_xls = pd.read_excel(path_system(), sheet_name=sheets[0])[
                                 ['id', 'ubicacion', 'clave', 'cantidad']].to_dict('records')

    return get_date_xls


def divide_info():
    divide = 45
    out_info = [get_sheet()[i:i + divide]
                          for i in range(0, len(get_sheet()), divide)]

    return out_info


def extraction():
   choice_side = int(input(".: Elige un lado :.\n1.-Derecha\n2.-Izquierda\nElegir: "))

   while choice_side <= 0 or choice_side > 2:
       print("El valor introducido no es valido")
       choice_side = int(input("Elige de nuevo: "))

   list_choice = []


   if choice_side == 1:
       for j in range(0, len(divide_info()), 2):
           list_choice.append(divide_info()[j])
   elif choice_side == 2:
       for j in range(1, len(divide_info()), 2):
           list_choice.append(divide_info()[j])

   for k in list_choice:
       k.append({'id': 'id', 'ubicacion': 'ubicacion', 'clave': 'clave', 'cantidad': 'cantidad'})

   flat_list = list(itertools.chain(*list_choice))

   for i in tqdm(range(0, 100), total=len(flat_list),
                 desc="Cargando archivo: "):
       sleep(.1)

   return flat_list


def export_dates(lado):
    headers =  ['id', 'ubicacion', 'clave', 'cantidad']

    name_document = input("Por favor, Agrega un nombre al archivo: ")
    print(".: Cargando programa :.\n-----------------------")

    with open(name_document + lado + '.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(extraction())

    print("Archivo Creado con éxito !!!")


if __name__ == '__main__':
    export_dates("der")
    export_dates("izq")