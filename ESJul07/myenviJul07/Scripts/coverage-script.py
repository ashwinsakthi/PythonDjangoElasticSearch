#!c:\dev_coding\python-es\esjul07\myenvijul07\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'coverage==4.3.4','console_scripts','coverage'
__requires__ = 'coverage==4.3.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('coverage==4.3.4', 'console_scripts', 'coverage')()
    )
