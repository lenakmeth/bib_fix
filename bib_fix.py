#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Capitalize the titles of articles automatically for LaTeX bibliography.
"""

import sys


def replace_quotations(string):
	""" Replaces first character in double quotations with LaTeX syntax."""
	correct = ''
	string = string.split()
	# single quotations - TODO?

	# double quotations
	indices = [idx for idx, char in enumerate(string) if char == '"']
	if len(indices) > 1:
		for char in string:
			if not string.index(char) in indices:
				correct += char
			else:
				if string.index(char) % 2 != 0:
					correct += '``'
				else:
					correct += char
	else:
		correct = ''.join(string)

	return correct

# open your file
with open(sys.argv[1], 'r') as f:
    lines = [l.strip() for l in f]
    
new_lines = []
for l in lines:
    
    # no indentation for first line of each publication
    if l.startswith('@'):
        new_lines.append(l)
        
    # wrap capitals with {} for title, add indentation
    elif l.startswith('title'):
        temp = ''
        for char in l.split('=')[1]:
            if char.isupper():
                temp += '{' + char + '}'
            else:
                temp += char

        temp = '{' + temp[1:-1].replace('}{', '').replace('{{', '').replace('}}', '') + '}' 
    
    	# replace " " with latex syntax

        new_lines.append('\ttitle =\t' + temp)
      
    # other lines need indentation too
    elif len(l.split('=')) == 2:
        new_lines.append('\t' + l.split('=')[0] + ' =\t' + l.split('=')[1])
        
    # whitelines
    else:
        new_lines.append(l)
        
# write file
with open(sys.argv[2], 'w') as f:
    for l in new_lines:
        f.write(l + '\n')