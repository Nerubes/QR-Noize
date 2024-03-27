import treepoem
import sys
import os

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
        barcode.save(dir_path + "/" + str(index) + ".jpg")
        index += 1
        amount -= 1
        if amount == 0:
            is_set = False
    else:
        parsed = line.split(":")
        barcode_type = parsed[0]
        amount = int(parsed[1])
        options = None #TODO:Make actual options
        is_set = True