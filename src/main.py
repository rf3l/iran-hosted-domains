import os

import requests
import xlrd
import json

from constants import *
from custom_domains import *
from utils import *
from functools import reduce


def download(url: str, path: str):
    if not os.path.exists(path):
        r = requests.get(url, allow_redirects=True, verify=False)
        with open(path, "wb") as file:
            file.write(r.content)
            file.close()


def g2b_ito_gov() -> set:
    download(g2b_gov_url, g2b_gov_file_path)

    workbook = xlrd.open_workbook(g2b_gov_file_path, ignore_workbook_corruption=True)
    sheet = workbook.sheet_by_index(0)

    data = (sheet.row_values(row)[0] for row in range(sheet.nrows))
    return set(map(lambda x: cleanup(x), data))


def adsl_tci() -> set:
    download(adsl_tci_url, adsl_tci_file_path)

    # Skip first 2 lines!
    with open(adsl_tci_file_path, "r") as file:
        next(file)
        next(file)
        lines = file.readlines()

    return set(map(lambda x: cleanup(x.strip()), lines))


def save_to_file(path, content):
    with open(path, "w") as file:
        file.write(content)


def create_qv2ray_schema(directs: list, proxies: list):
    schema = {
        "description": "Iran hosted domains",
        "domainStrategy": "AsIs",
        "domains": {
            "direct": ["regexp:^.+\\.ir$"] + directs,
            "proxy": proxies,
            "block": ["geosite:category-ads-all"]
        },
        "ips": {
            "direct": ["geoip:ir"]
        },
        "name": "ir_hosted"
    }
    save_to_file(qv2ray_schema_path, json.dumps(schema))


if __name__ == "__main__":
    if not os.path.exists("download"):
        os.mkdir("download")
    if not os.path.exists("output"):
        os.mkdir("output")

    # Proxy domains
    proxy_domains = sorted(set(custom_domains["proxy"]))

    # Request data from sources and cleanup
    sets = [g2b_ito_gov(), adsl_tci(), set(custom_domains["direct"])]

    # Filter extras
    full_domains = reduce(lambda x, y: x.union(y), sets)
    full_domains = filter(lambda x: is_url(x), full_domains)
    full_domains = filter(lambda x: not is_ip(x), full_domains)
    full_domains = map(lambda x: convert_utf8(x), full_domains)
    full_domains = set(full_domains)

    # Divide info
    ir_domains = set(filter(lambda x: is_ir(x), full_domains))
    other_domains = full_domains.difference(ir_domains)

    # Sort
    ir_domains = sorted(ir_domains)
    other_domains = sorted(other_domains)

    # Generate output files
    save_to_file(ir_domains_path, "\n".join(ir_domains))
    save_to_file(other_domains_path, "\n".join(other_domains))
    create_qv2ray_schema(other_domains, proxy_domains)
