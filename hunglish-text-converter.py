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
	"^": "/"
}

for line in sys.stdin:
	for key in char_dict:
		line = line.replace(key, char_dict[key])
	sys.stdout.write(line)