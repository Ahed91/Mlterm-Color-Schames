#!/usr/bin/env python
# encoding: utf-8

"""
convert colorshame from xrdb to mlterm
"""
from pathlib import Path
import re
import os


def convert_xrdb_to_list(line):
    key = re.split(r'_Color', line)[0].replace('#define ', '')
    value = re.split(r'_Color', line)[1].strip()
    return [key, value]


def convert(xrdb_path):
    xrdb_mlterm_mapping = {
        'Ansi_0': 'black',
        'Ansi_1': 'red',
        'Ansi_2': 'green',
        'Ansi_3': 'yellow',
        'Ansi_4': 'blue',
        'Ansi_5': 'magenta',
        'Ansi_6': 'cyan',
        'Ansi_7': 'white',
        'Ansi_8': 'hl_black',
        'Ansi_9': 'hl_red',
        'Ansi_10': 'hl_green',
        'Ansi_11': 'hl_yellow',
        'Ansi_12': 'hl_blue',
        'Ansi_13': 'hl_magenta',
        'Ansi_14': 'hl_cyan',
        'Ansi_15': 'hl_white',
        'Foreground': 'fg_color',
        'Background': 'bg_color',
        # 'Badge': None,
        'Cursor': 'cursor_bg_color',
        # 'Cursor_Guide': None,
        'Cursor_Text': 'cursor_fg_color',
        'Bold': 'bd_color',
        # 'Link': None,
        'Selected_Text': 'it_color',
        'Selection': 'ul_color'
    }

    for file in xrdb_path.glob('*.xrdb'):
        # read xrdb file
        with open('../xrdb/%s' % file, 'r') as f:
            data = f.readlines()

        data = list(map(convert_xrdb_to_list, data))
        current_xrdb_color = {item[0]: item[1] for item in data}
        current_mlterm_color = {}

        for key in xrdb_mlterm_mapping:
            if key in current_xrdb_color:
                current_mlterm_color[xrdb_mlterm_mapping[key]] = current_xrdb_color[key]

        current_mlterm_color_list = [k + "=" + v for k, v in current_mlterm_color.items()]
        current_mlterm_color_string = "\n".join(current_mlterm_color_list)

        new_file = file.name.replace('xrdb', 'color')
        # open mlterm color file for write
        with open('../xrdb/' + new_file, 'w') as new_f:
            new_f.write(current_mlterm_color_string)


def main():
    # Set xrdb folder path
    xrdb_path = Path('../xrdb/')

    convert(xrdb_path)

if __name__ == "__main__":
    main()
