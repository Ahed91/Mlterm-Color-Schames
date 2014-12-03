#!/usr/bin/env python
# encoding: utf-8

"""
convert colorshame from xrdb to mlterm
"""
import re
import os

# Get the files
files = os.listdir('../xrdb/')

# every term in xrdb and its opposite in mlterm
dict={'Ansi_0_Color':'black','Ansi_1_Color':'red','Ansi_2_Color':'green','Ansi_3_Color':'yellow','Ansi_4_Color':'blue','Ansi_5_Color':'magenta','Ansi_6_Color':'cyan','Ansi_7_Color':'white','Ansi_8_Color':'hl_black','Ansi_9_Color':'hl_red','Ansi_10_Color':'hl_green','Ansi_11_Color':'hl_yellow','Ansi_12_Color':'hl_blue','Ansi_13_Color':'hl_magenta','Ansi_14_Color':'hl_cyan','Ansi_15_Color':'hl_white','Background_Color':'bg_color','Bold_Color':'bd_color','Cursor_Color':'cursor_bg_color','Cursor_Text_Color':'cursor_fg_color','Foreground_Color':'fg_color','Selected_Text_Color':'it_color','Selection_Color':'ul_color'}

for i in range(116):
    # read xrdb file
    with open('../xrdb/%s'%files[i], 'r') as f:
        # make new file the same name but differnet ext.
        new_file=files[i].replace('xrdb','color')
        # open mlterm color file for write
        with open(new_file,'w') as new_f:
            for line in f.readlines():
                # Delelte '#define' string
                line = line.replace('#define ','')
                # replace space with =
                line = line.replace(' ','=')
                # use re to match right expression with its mlterm opposite
                match=re.findall('(.*_Color)',line)[0]
                line = line.replace(match,dict[match])
                # write line
                new_f.writelines(line)                        

files = os.listdir('.')
data=[]

for i in range(116):
    with open(files[i],'r') as f:
        data = f.readlines()
        data.insert(2,data[8])
        data.insert(3,data[10])
        data.insert(4,data[12])
        data.insert(5,data[14])
        data.insert(6,data[16])
        data.insert(7,data[18])
        data.insert(8,data[20])
        data.insert(9,data[22])
        print data, files[i]
        data.insert(24,data[28])
        data.insert(29,data[26])
        data.pop(16)
        data.pop(16)
        data.pop(16)
        data.pop(16)
        data.pop(16)
        data.pop(16)
        data.pop(16)
        data.pop(16)
        data.pop(18)
        data.pop(21)
     

    with open(files[i],'w') as f:
        f.writelines(data)

