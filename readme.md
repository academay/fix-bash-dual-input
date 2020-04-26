hebfix
=======

Purpose:
------

Fix accidental typing in non-english keyboatrd layout:

 1. inside bash (console)
 2. in any GUI text input box where the cursor is positioned.


WARNING:
==========
this is pre-alpha version,
tested only on 1 machine (ubuntu 16+kde)


1. bash hebfix
================
Fixes accidental hebrew commands.

limitation: there's no autocomplete in bash. An alternative solution could be - creating symlinks in hebrew to EVERY command. However that's not feasible with bash built-in functions...

Install instructions:

Before install:
---------------
the bash hook mechanism can't handle aliases.
Solution:

 - convert all your aliases into bash functions (they're better anyway).

How to install:
---------------
   cp .heb2eng ~/
   sudo cp heb2eng-bash-little-helper.py /usr/local/bin
   sourcecmd="source ~/.heb2eng.sh"
   if ! grep -Fxq "$sourcecmd" ~/.bashrc ; then
      echo "$sourcecmd" >> ~/.bashrc
   fi



2. GUI textbox:
=================
Not implemented (half backed, really).
This one uses keyboard commands, sendkeys alternatives, and clipboard manipulations.
Written in python




פתרון לכתיבה בעברית (בטעות) בתוך bash
או - "איך להריץ פקודה שהוקלדה במצב עברית?"
הבעיה:
כשאני על מקלדת עברית, פותח טרמינל, מקיש
user@machine $ ls
אבל יוצא לי
user@machine $ ךד
l ךד: command not found

הפתרון שלי כרגע:
-------------------
חיבור hook ל-BASH שפועל אחרי הקלדת הפקודה אבל לפני ההרצה שלה
קריאה לתוכנית חיצונית (במקרה שלי פייתון) שבודקת האם הפקודה מתחילה בעברית, ואז מסיקה שהמקלדת הפוכה, ומחליפה את האותיות לפי מיפוי מקלדות.
דחיפה של הפקודה המתוקנת (לפי הצורך)



