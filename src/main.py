import os

import requests
import xlrd

from constants import *
from utils import *


def download(url: str, path: str):
    if not os.path.exists(path):
        r = requests.get(url, allow_redirects=True, verify=False)
        with open(path, 'wb') as file:
            file.write(r.content)
            file.close()


def g2b_ito_gov():
    download(g2b_gov_url, g2b_gov_file_path)

    workbook = xlrd.open_workbook(g2b_gov_file_path, ignore_workbook_corruption=True)
    sheet = workbook.sheet_by_index(0)

    data = [sheet.row_values(row)[0] for row in range(sheet.nrows)]
    return set(map(lambda x: cleanup(x), data))


def adsl_tci():
    download(adsl_tci_url, adsl_tci_file_path)

    # Skip first 2 lines!
    file = open(adsl_tci_file_path, "r")
    next(file)
    next(file)
    lines = file.readlines()

    return set(map(lambda x: cleanup(x.strip()), lines))


if __name__ == '__main__':
    if not os.path.exists("download"):
        os.mkdir("download")

    g2b_set = g2b_ito_gov()
    x_set = adsl_tci()

    full_domains = g2b_set.union(x_set)
    full_domains = set(filter(lambda x: is_url(x), full_domains))
    full_domains = set(filter(lambda x: not is_ip(x), full_domains))

    ir_domains = set(filter(lambda x: is_ir(x), full_domains))
    other_domains = full_domains.difference(ir_domains)

    if not os.path.exists("data"):
        os.mkdir("data")

    with open(ir_domains_path, "w") as file:
        data = list(ir_domains)
        data.sort()
        file.write("\n".join(data))

    with open(other_domains_path, "w") as file:
        data = list(other_domains)
        data.sort()
        file.write("\n".join(data))
