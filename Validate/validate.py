import zxingcpp
import cv2
import sys
import os
import json

JSON_NEW_ANNOTATION_NAME = "validation.json"
JSON_ANNOTATION_NAME = "annotation.json"

mod_img_path = sys.argv[1]
orig_img_path = sys.argv[2]

annotations_dict = {}

with open(os.path.join(orig_img_path, JSON_ANNOTATION_NAME), 'r') as f:
    annotations_dict = json.load(f)
decoded_dict = {}

for img in os.listdir(mod_img_path):
    img_mat = cv2.imread(os.path.join(mod_img_path, img))
    if not (img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png')):
        if not img.endswith('.json'):
            print("Warning: ", img, " is not image!")
        continue
    result = zxingcpp.read_barcodes(img_mat)
    info = annotations_dict[img.split('_')[0]]
    decoded_dict[img] = info
    #not used now
    decoded_dict[img]["distorted"] = 0
    decoded_dict[img]["restored"] = len(result) > 0

with open(os.path.join(mod_img_path, JSON_NEW_ANNOTATION_NAME), '+w') as f:
    json.dump(decoded_dict, f)