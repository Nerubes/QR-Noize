import sys
import os
import json
import augraphy

JSON_ANNOTAION_NAME = "annotation.json"

annotsion_list = {}

def real_destorts(d):
    by_line_dist = d.split('\n')
    name = by_line_dist[0]
    if name[0] == '/':
        return '', []
    pipeline = []
    for i in by_line_dist:
        params = i.split(' ')
        if params[0] == 'LightingGradient' and len(params) == 8:
            x, y = int(params[1]), int(params[2])
            if x == -1 or y == -1:
                direction = float(params[3])
                max_br, min_br = int(params[4]), int(params[5])
                mode = params[6]
                p = float(params[7])
                pipeline.append(augraphy.LightingGradient(direction=direction, 
                                                          max_brightness=max_br, 
                                                          min_brightness=min_br, 
                                                          mode=mode, p=p))
            else:
                pipeline.append(augraphy.LightingGradient(light_position=(x, y),
                                                          direction=direction, 
                                                          max_brightness=max_br, 
                                                          min_brightness=min_br, 
                                                          mode=mode, p=p))
        if params[0] == 
    return name, pipeline

in_dir_path = sys.argv[1]
out_dir_path = sys.argv[2]
config_path = sys.argv[3]

try:
    os.mkdir(out_dir_path)
    print(f"Making directory : {out_dir_path}")
except FileExistsError:
    print("Directory already exists")

tmp_distorts = []

with open("config_psth", 'r') as f:
    tmp_distorts = f.read().split("\n\n")[:-1]