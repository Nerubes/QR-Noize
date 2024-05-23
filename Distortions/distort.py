import sys
import os
import json
import augraphy
import cv2

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
            direction = float(params[3])
            max_br, min_br = int(params[4]), int(params[5])
            mode = params[6]
            p = float(params[7])
            if x == -1 or y == -1:
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
        elif params[0] == 'ReflectedLight' and len(params) == 7:
            x, y = int(params[1]), int(params[2])
            minor_major_ratio = float(params[3])
            max_br, min_br = int(params[4]), int(params[5])
            p = float(params[6])
            if x == -1 or y == -1:
                pipeline.append(augraphy.LightingGradient(direction=direction, 
                                                          max_brightness=max_br, 
                                                          min_brightness=min_br, 
                                                          p=p))
            else:
                pipeline.append(augraphy.LightingGradient(light_position=(x, y),
                                                          direction=direction, 
                                                          max_brightness=max_br, 
                                                          min_brightness=min_br, 
                                                          p=p))
        else:
            raise f"Unknown line: \"{d}\""
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


for i in tmp_distorts:
    name, d = real_destorts(i)
    for img in os.listdir(in_dir_path):
        img_mat = cv2.imread(os.path.join(in_dir_path, img))
        if not (img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png')):
            if not img.endswith('.json'):
                print("Warning: ", img, " is not image!")
            continue

        for func in d:
            img_mat = func(img_mat)

        extension = img.split('.')[-1]
        img_name = '.'.join(img.split('.')[0:-1])
        new_name = img_name + '_' + name + '_' + extension

        cv2.imwrite(new_name, img_mat)