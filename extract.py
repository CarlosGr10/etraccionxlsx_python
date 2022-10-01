import re
import pandas as pd
import pathlib
import os

def path_system():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'CPdescarga.xls')
    return my_file


def get_sheets(state_id):
    xls = pd.ExcelFile(path_system())
    sheets = xls.sheet_names
    get_dates_xls = pd.read_excel(path_system(), sheet_name=sheets[state_id])[['d_estado', 'd_codigo' ,'d_asenta' ,'d_ciudad']].to_dict('records')
    return get_dates_xls


def get_fake_dates(id):
    example = [[{'d_estado': 'Aguascalientes', 'd_codigo': 20957, 'd_asenta': 'El Rincón de la Virgen (El Rincón)', 'd_ciudad': 'nan'},],
    [{'d_estado': 'Aguascalientes', 'd_codigo': 20970, 'd_asenta': 'Puente de Villalpando (El Puente)', 'd_ciudad': 'nan'},],
    [{'d_estado': 'Aguascalientes', 'd_codigo': 20955, 'd_asenta': 'San Rafael', 'd_ciudad': 'nan'}]]
    election = example[id]

    return election


if __name__ == '__main__':
    print(get_sheets(1))
    