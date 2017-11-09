#!/usr/bin/python

import sys

# <from (eng)>: <to (hun)>
char_dict = {
	"'": "á", "\"": "Á",
	";": "é", ":": "É",
	"`": "í", "~": "Í",
	"=": "ó", "+": "Ó",
	"0": "ö", ")": "Ö",
	"[": "ő", "{": "Ő",
	"]": "ú", "}": "Ú",
	"-": "ü", "_": "Ü",
	"\\": "ű", "|": "Ű",
	"y": "z", "Y": "Z",
	"z": "y", "Z": "Y",
	"/": "-",
	"?": "_",
	"<": "?",
	">": ":",
	"$": "!",
	"¢": "$",
	"!": "'",
	"@": "\"",
	"œ": "@",
	"‹": "#",
	"¯": "*",
	"^": "/",
	"æ": "^"
}

for line in sys.stdin:
	new_line = ''
	for char in line:
		if (char in char_dict):
			new_line += char_dict[char]
		else:
			new_line += char
	sys.stdout.write(new_line)