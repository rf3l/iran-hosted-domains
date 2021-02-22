import os

import requests
import xlrd

from src.constants import *
from src.utils import *


def g2b_ito_gov():
    r = requests.get(g2b_gov_url, allow_redirects=True, verify=False)
    with open(g2b_gov_file_path, 'wb') as file:
        file.write(r.content)
        file.close()

    workbook = xlrd.open_workbook(g2b_gov_file_path, ignore_workbook_corruption=True)
    sheet = workbook.sheet_by_index(0)

    data = [sheet.row_values(row)[0] for row in range(sheet.nrows)]
    data = map(lambda x: cleanup(x), data)
    return set(data)


def adsl_tci():
    r = requests.get(adsl_tci_url, allow_redirects=True)
    with open(adsl_tci_file_path, 'wb') as file:
        file.write(r.content)
        file.close()

    file = open(adsl_tci_file_path, "r")

    # Skip first 2 lines!
    next(file)
    next(file)
    lines = file.readlines()

    data = map(lambda x: cleanup(x.strip()), lines)
    return set(data)


if __name__ == '__main__':
    if not os.path.exists("download"):
        os.mkdir("data")

    g2b_set = g2b_ito_gov()
    x_set = adsl_tci()

    full_domains = g2b_set.union(x_set)
    full_domains = set(filter(lambda x: is_url(x), full_domains))

    ir_domains = set(filter(lambda x: is_ir(x), full_domains))
    other_domains = full_domains.difference(ir_domains)

    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/ir_domains", "w") as file:
        data = list(ir_domains)
        data.sort()
        file.write("\n".join(data))

    with open("data/other_domains", "w") as file:
        data = list(other_domains)
        data.sort()
        file.write("\n".join(data))
