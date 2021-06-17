#!/usr/bin/env python
# encoding: utf-8

import os
import shutil
import argparse
import re
import subprocess

def get():
    "Get colorschames"
    os.makedirs(os.path.expanduser('~/.mlterm/colorschames'))
    data_folder = './mlterm/colorschames' 
    dest_folder = os.path.expanduser('~/.mlterm/colorschames')
    for _ in os.listdir(data_folder):
        __ = os.path.join(data_folder, _)
        shutil.copy(__, dest_folder)

def list_colorschemes():
    colorschame_list = os.listdir(os.path.expanduser('~/.mlterm/colorschames'))
    for cs in colorschame_list:
        print(cs)

def check_color(color):
    colorschame_list = os.listdir(os.path.expanduser('~/.mlterm/colorschames'))
    legal_color = False
    for idx, item in enumerate(colorschame_list):
        if color == item :
            legal_color = True
            return colorschame_list[idx], legal_color
        item = item.lower()
        if color == item :
            legal_color = True
            return colorschame_list[idx],  legal_color
        item = item.upper()
        if color == item :
            legal_color = True
            return colorschame_list[idx],  legal_color
        item = item.replace('.COLOR', '')
        if color == item :
            legal_color = True
            return colorschame_list[idx],  legal_color
        item = item.lower()
        if color == item :
            legal_color = True
            return colorschame_list[idx],  legal_color
        item = item.replace(item[0], item[0].upper())
        if color == item :
            legal_color = True
            return colorschame_list[idx],  legal_color

    return 'none',legal_color

def set_color(name):
    colors_path = os.path.expanduser('~/.mlterm/colorschames')
    main_path = os.path.expanduser('~/.mlterm/main')
    color_path = os.path.join(colors_path, name)
    lines=""

    with open(color_path, 'r') as f :
        data = f.readlines()
    with open(os.path.expanduser('~/.mlterm/color'), 'w') as f :
        f.writelines(data[0:16])
    
    D = {}
    for i,item in enumerate(data[16:23]):
        D[i] = item

    if os.path.exists(main_path):
        with open(main_path, 'r') as f :
            lines = f.readlines()

    with open(main_path, 'w') as f :
        for line in lines:
            if re.findall('^fg_color.*', line):
                f.write(re.sub('^fg_color.*',D.pop(0).replace('\n','') , line))
                continue
            if re.findall('^bg_color.*', line):
                f.write(re.sub('^bg_color.*',D.pop(1).replace('\n','') , line))
                continue
            if re.findall('^cursor_bg_color.*', line):
                f.write(re.sub('^cursor_bg_color.*',D.pop(2).replace('\n','') , line))
                continue
            if re.findall('^cursor_fg_color.*', line):
                f.write(re.sub('^cursor_fg_color.*',D.pop(3).replace('\n','') , line))
                continue
            if re.findall('^bd_color.*', line):
                f.write(re.sub('^bd_color.*',D.pop(4).replace('\n','')  , line))
                continue
            if re.findall('^it_color.*', line):
                f.write(re.sub('^it_color.*',D.pop(5).replace('\n','') , line))
                continue
            if re.findall('^ul_color.*', line):
                f.write(re.sub('^ul_color.*',D.pop(6).replace('\n','') , line))
                continue
            if re.findall('^#fg_color.*', line):
                f.write(re.sub('^#fg_color.*',D.pop(0).replace('\n','') , line))
                continue
            if re.findall('^#bg_color.*', line):
                f.write(re.sub('^#bg_color.*',D.pop(1).replace('\n','') , line))
                continue
            if re.findall('^#cursor_bg_color.*', line):
                f.write(re.sub('^#cursor_bg_color.*',D.pop(2).replace('\n','') , line))
                continue
            if re.findall('^#cursor_fg_color.*', line):
                f.write(re.sub('^#cursor_fg_color.*',D.pop(3).replace('\n','') , line))
                continue
            if re.findall('^#bd_color.*', line):
                f.write(re.sub('^#bd_color.*',D.pop(4).replace('\n','')  , line))
                continue
            if re.findall('^#it_color.*', line):
                f.write(re.sub('^#it_color.*',D.pop(5).replace('\n','') , line))
                continue
            if re.findall('^#ul_color.*', line):
                f.write(re.sub('^#ul_color.*',D.pop(6).replace('\n','') , line))
                continue
            if re.findall('^wall_picture.*', line):
                f.write(line.replace('~', os.path.expanduser('~')))
                continue
            f.write(line)
        for _ in D.keys():
            f.write(D[_])

def main():
    """Execute"""
    # Parser Options
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--colorschame', help="choose colorschame to apply on mlterm")
    parser.add_argument('-l','--list', help="list colorschames", action="store_true")
    #parser.add_argument('--pic', help="set wallpaper for mlterm", action="store_true")
    args = parser.parse_args()

    if not os.path.exists(os.path.expanduser('~/.mlterm/colorschames')):
        get()

    if args.list:
        list_colorschemes()
        exit()

    [name,legal]=check_color(args.colorschame)
    if not legal:
        print('Invalid or Unavailable Colorschame Name ')

    if legal:
        set_color(name)

if __name__ == '__main__':
    main()
