import treepoem
import sys
import os
import json

JSON_ANNOTAION_NAME = "annotation.json"

annotsion_list = {}

def parse_options(opt):
    if opt[0].startswith("None"):
        return None
    options = dict()
    for i in opt:
        key, value = i.split("=")
        options[key.strip()] = value.strip() 
    return options

config_path = sys.argv[1]
dir_path = sys.argv[2]
try:
    os.mkdir(dir_path)
    print(f"Making directory : {dir_path}")
except FileExistsError:
    print("Directory already exists")

config = open(config_path, 'r')
config_lines = config.readlines()

is_set = False
barcode_type = None
amount = 0
options = None

index = 0

for line in config_lines:
    if is_set:
        barcode = treepoem.generate_barcode(barcode_type=barcode_type, data=line.strip(), options=options)
        barcode.save(f"{dir_path}/{str(index)}.png")
        annotsion_list[index] = {"value":line.strip(), "type":barcode_type, "options":options}
        index += 1
        amount -= 1
        if amount == 0:
            is_set = False
    else:
        parsed = line.split(":")
        barcode_type = parsed[0]
        amount = int(parsed[1])
        options = parse_options(parsed[2:])
        is_set = True

with open(f"{dir_path}/{JSON_ANNOTAION_NAME}", "w") as f:
    json.dump(annotsion_list, f)