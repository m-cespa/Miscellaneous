# American to English date converter

import re, os, shutil

pattern = re.compile(r"""^(.*?)         # all text before the date
                     ((0|1)?\d)-        # month
                     ((0|1|2|3)?\d)-    # day
                     ((19|20)\d\d)      # year, restricted to 1900, 2000
                     (.*?)$             # all text after the date
                     """, re.VERBOSE)

# loop over files in cwd
for amerFileName in os.listdir('.'):
    mo = pattern.search(amerFileName)

    if mo == None:
        continue

    beftext = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    aftext = mo.group(8)

# forming English date syntax
    newFileName = beftext + day + '-' + month + '-' + year + aftext
# get absolute path for cwd
    abswd = os.path.abspath('.')
# create string path for current file in cwd
    amerFileName = os.path.join(abswd, amerFileName)
    newFileName = os.path.join(abswd, newFileName)
    shutil.move(amerFileName, newFileName)

