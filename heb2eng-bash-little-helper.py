#!/usr/bin/env python
# https://github.com/academay/fix-bash-dual-input/new/master
# 2020-04-26

import os,sys

args = sys.argv[1:]
arg1 = args[0][0]

d = {
'א': 't',
'ב': 'c',
'ג': 'd',
'ד': 's',
'ה': 'v',
'ו': 'u',
'ז': 'z',
'ח': 'j',
'ט': 'y',
'י': 'h',
'כ': 'f',
'ך': 'l',
'ל': 'k',
'מ': 'n',
'ם': 'o',
'נ': 'b',
'ן': 'i',
'ס': 'x',
'ע': 'g',
'פ': 'p',
'ף': ';',
'צ': 'm',
'ץ': '.',
'ק': 'e',
'ר': 'r',
'ש': 'a',
'ת': ',',
"'": "w",
',': "'",
'ף': ';',
'ץ': '.',
'.': '/',
}

cmd = ''
for arg in args:
    if ' 'in arg or '\t' in arg:
        arg = '"' + arg + '"'
    cmd = cmd + ' ' + arg

#print(arg1)
if arg1 in "אבגדהוזחטיכךלמםנןסעפףצץקרשת'":
    cmd = ''.join([d.get(c, c) for c in cmd])   # translate

#os.system(cmd)
print(cmd)

